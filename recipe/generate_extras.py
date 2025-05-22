#!/usr/bin/env python

# A script for removing and regeneratingg the {{ name }}-with-<extra> outputs
# in meta.yaml from the pyproject.toml file from the latest Apache Airflow
# release.

# Requires a conda environment with the toml package

import argparse
import re
import sys
from pathlib import Path

import toml


def parse_optional_deps(pyproject_path):
    """
    Parse the [project.optional-dependencies] section from a pyproject.toml file.

    Args:
        pyproject_path (str or Path): Path to the pyproject.toml file.

    Returns:
        dict: Dictionary of optional dependencies.
    """
    pyproject = toml.load(pyproject_path)
    return pyproject["project"]["optional-dependencies"]


def remove_with_extra_outputs(meta_text):
    """
    Remove all outputs with name: airflow-with-<extra> from the meta.yaml text,
    including any trailing blank lines until the next block of text.

    Args:
        meta_text (str): The contents of meta.yaml.

    Returns:
        str: The meta.yaml text with airflow-with-<extra> outputs removed.
    """
    pattern = re.compile(
        r"(?m)^[ \t]*- name: {{ name }}-with-[\w\-]+\n(?:[ \t]+.*\n)+((?:[ \t]*\n)*)"
    )
    return pattern.sub("", meta_text)


def generate_output_block(extra, deps):
    """
    Generate a YAML output block for a given extra and its dependencies.

    Args:
        extra (str): The name of the extra.
        deps (list): The dependencies for the extra.

    Returns:
        str or None: The YAML block as a string, or None if not a recognized extra.
    """
    if extra == "all":
        reqs = []
        for dep in deps:
            dep = replace_bracket_extras_with_with_extra(dep)
            if dep.startswith("apache-airflow-core["):
                core_extra = dep.split("[", 1)[1].split("]", 1)[0]
                reqs.append(f"apache-airflow-core-with-{core_extra}")
            elif dep.startswith("apache-airflow-providers-"):
                req = dep
                if ">=" in req and not re.search(r"\s>=", req):
                    req = req.replace(">=", " >=")
                reqs.append(req)
        if not reqs:
            return None
        reqs_yaml = "\n".join(f"        - {r}" for r in reqs)
        block = f"""  - name: {{{{ name }}}}-with-all
    build:
      noarch: python
    requirements:
      host:
        - python {{{{ python_min }}}}
      run:
        - python >={{{{ python_min }}}},<{{{{ python_over }}}}
        - {{{{ pin_subpackage(name, max_pin='x.x.x.x.x.x') }}}}
{reqs_yaml}
    test:
      imports:
        - airflow
      commands:
        - pip check
      requires:
        - python {{{{ python_min }}}}
        - pip

"""
        return block
    # Determine if this is a core extra or a provider extra
    if deps and isinstance(deps, list) and deps[0].startswith("apache-airflow-core["):
        # core extra
        core_extra = deps[0].split("[", 1)[1].split("]", 1)[0]
        req = f"apache-airflow-core-with-{core_extra}"
    elif deps and isinstance(deps, list) and deps[0].startswith("apache-airflow-providers-"):
        # provider extra
        req = deps[0]
        if ">=" in req and not re.search(r"\s>=", req):
            req = req.replace(">=", " >=")
    else:
        # skip unknown
        return None

    extra = extra.replace(".", "-")

    block = f"""  - name: {{{{ name }}}}-with-{extra}
    build:
      noarch: python
    requirements:
      host:
        - python {{{{ python_min }}}}
      run:
        - python >={{{{ python_min }}}},<{{{{ python_over }}}}
        - {{{{ pin_subpackage(name, max_pin='x.x.x.x.x.x') }}}}
        - {req}
    test:
      imports:
        - airflow
      commands:
        - pip check
      requires:
        - python {{{{ python_min }}}}
        - pip

"""
    return block


def expand_airflow_extras(deps_to_keep, optional_deps):
    """
    For each extra in deps_to_keep, if its dependencies include 'apache-airflow[extra1,extra2,...]',
    expand those extras by adding the dependencies from optional_deps for each referenced extra.
    """
    for extra, deps in deps_to_keep.items():
        new_deps = []
        for dep in deps:
            m = re.match(r"apache-airflow\[(.*?)\]", dep)
            if m:
                extras_list = [e.strip() for e in m.group(1).split(",")]
                for sub_extra in extras_list:
                    # Only add if present in optional_deps
                    if sub_extra in optional_deps:
                        new_deps.extend(optional_deps[sub_extra])
            else:
                new_deps.append(dep)
        deps_to_keep[extra] = new_deps


def replace_bracket_extras_with_with_extra(dep):
    """
    For apache-airflow-providers-common-sql and apache-airflow-providers-amazon,
    replace '[<extra>]' in dependency strings with '-with-<extra>'.
    E.g., 'apache-airflow-providers-common-sql[pandas]' -> 'apache-airflow-providers-common-sql-with-pandas'
    """
    for base in ("apache-airflow-providers-common-sql", "apache-airflow-providers-amazon"):
        m = re.match(rf"({base})\[(.*?)\](.*)", dep)
        if m:
            extras = m.group(2).replace(",", "-")
            return f"{base}-with-{extras}{m.group(3)}"
    return dep


def main():
    """
    Main entry point for the script. Parses arguments, reads pyproject.toml and meta.yaml,
    generates new outputs for extras, and writes the updated meta.yaml.
    """
    parser = argparse.ArgumentParser(
        description="Generate airflow -with-<extra> outputs for meta.yaml from pyproject.toml"
    )
    parser.add_argument("pyproject", help="Path to pyproject.toml")
    parser.add_argument("meta", help="Path to meta.yaml")
    args = parser.parse_args()

    pyproject_path = args.pyproject
    meta_path = args.meta
    out_path = Path(meta_path).parent / "meta-updated-extras.yaml"

    with open(meta_path) as f:
        meta_text = f.read()

    # Remove all -with-<extra> outputs
    meta_text_clean = remove_with_extra_outputs(meta_text)

    # Find where to insert outputs (after the last main output)
    outputs_match = re.search(r"(?ms)^outputs:\n(.*?)(?=^about:|^extra:|^\Z)", meta_text_clean)
    if not outputs_match:
        print("Could not find outputs section in meta.yaml")
        sys.exit(1)
    outputs_end = outputs_match.end(1)

    # Parse extras from pyproject.toml
    optional_deps = parse_optional_deps(pyproject_path)
    new_outputs = ""
    extras_to_keep = ['all-core', 'all']
    deps_to_keep = {
        k: v for k, v in optional_deps.items() if k in extras_to_keep
    }

    expand_airflow_extras(deps_to_keep, optional_deps)

    for extra, deps in deps_to_keep.items():
        block = generate_output_block(extra, deps)
        if block:
            new_outputs += block

    # Insert new outputs after the main outputs
    new_meta_text = (
        meta_text_clean[:outputs_end] + new_outputs + meta_text_clean[outputs_end:]
    )

    with open(out_path, "w") as f:
        f.write(new_meta_text)

    print(f"Updated meta.yaml with regenerated extras written to {out_path}")


if __name__ == "__main__":
    main()
