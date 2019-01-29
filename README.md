<!--
# -*- mode: jinja -*-
-->

About airflow-split
===================

Home: http://airflow.apache.org

Package license: Apache 2.0

Feedstock license: BSD 3-Clause

Summary: Airflow is a platform to programmatically author, schedule and monitor workflows

Use airflow to author workflows as directed acyclic graphs (DAGs)
of tasks. The airflow scheduler executes your tasks on an array of
workers while following the specified dependencies. Rich command
line utilities make performing complex surgeries on DAGs a snap.
The rich user interface makes it easy to visualize pipelines
running in production, monitor progress, and troubleshoot issues
when needed.

When workflows are defined as code, they become more maintainable,
versionable, testable, and collaborative.


Current build status
====================

[![Linux](https://img.shields.io/circleci/project/github/conda-forge/airflow-feedstock/master.svg?label=Linux)](https://circleci.com/gh/conda-forge/airflow-feedstock)
[![OSX](https://img.shields.io/travis/conda-forge/airflow-feedstock/master.svg?label=macOS)](https://travis-ci.org/conda-forge/airflow-feedstock)
![Windows disabled](https://img.shields.io/badge/Windows-disabled-lightgrey.svg)

Current release info
====================

| Name | Downloads | Version | Platforms |
| --- | --- | --- | --- |
| [![Conda Recipe](https://img.shields.io/badge/recipe-airflow-green.svg)](https://anaconda.org/conda-forge/airflow) | [![Conda Downloads](https://img.shields.io/conda/dn/conda-forge/airflow.svg)](https://anaconda.org/conda-forge/airflow) | [![Conda Version](https://img.shields.io/conda/vn/conda-forge/airflow.svg)](https://anaconda.org/conda-forge/airflow) | [![Conda Platforms](https://img.shields.io/conda/pn/conda-forge/airflow.svg)](https://anaconda.org/conda-forge/airflow) |
| [![Conda Recipe](https://img.shields.io/badge/recipe-airflow--with--async-green.svg)](https://anaconda.org/conda-forge/airflow-with-async) | [![Conda Downloads](https://img.shields.io/conda/dn/conda-forge/airflow-with-async.svg)](https://anaconda.org/conda-forge/airflow-with-async) | [![Conda Version](https://img.shields.io/conda/vn/conda-forge/airflow-with-async.svg)](https://anaconda.org/conda-forge/airflow-with-async) | [![Conda Platforms](https://img.shields.io/conda/pn/conda-forge/airflow-with-async.svg)](https://anaconda.org/conda-forge/airflow-with-async) |
| [![Conda Recipe](https://img.shields.io/badge/recipe-airflow--with--azure_blob_storage-green.svg)](https://anaconda.org/conda-forge/airflow-with-azure_blob_storage) | [![Conda Downloads](https://img.shields.io/conda/dn/conda-forge/airflow-with-azure_blob_storage.svg)](https://anaconda.org/conda-forge/airflow-with-azure_blob_storage) | [![Conda Version](https://img.shields.io/conda/vn/conda-forge/airflow-with-azure_blob_storage.svg)](https://anaconda.org/conda-forge/airflow-with-azure_blob_storage) | [![Conda Platforms](https://img.shields.io/conda/pn/conda-forge/airflow-with-azure_blob_storage.svg)](https://anaconda.org/conda-forge/airflow-with-azure_blob_storage) |
| [![Conda Recipe](https://img.shields.io/badge/recipe-airflow--with--cassandra-green.svg)](https://anaconda.org/conda-forge/airflow-with-cassandra) | [![Conda Downloads](https://img.shields.io/conda/dn/conda-forge/airflow-with-cassandra.svg)](https://anaconda.org/conda-forge/airflow-with-cassandra) | [![Conda Version](https://img.shields.io/conda/vn/conda-forge/airflow-with-cassandra.svg)](https://anaconda.org/conda-forge/airflow-with-cassandra) | [![Conda Platforms](https://img.shields.io/conda/pn/conda-forge/airflow-with-cassandra.svg)](https://anaconda.org/conda-forge/airflow-with-cassandra) |
| [![Conda Recipe](https://img.shields.io/badge/recipe-airflow--with--celery-green.svg)](https://anaconda.org/conda-forge/airflow-with-celery) | [![Conda Downloads](https://img.shields.io/conda/dn/conda-forge/airflow-with-celery.svg)](https://anaconda.org/conda-forge/airflow-with-celery) | [![Conda Version](https://img.shields.io/conda/vn/conda-forge/airflow-with-celery.svg)](https://anaconda.org/conda-forge/airflow-with-celery) | [![Conda Platforms](https://img.shields.io/conda/pn/conda-forge/airflow-with-celery.svg)](https://anaconda.org/conda-forge/airflow-with-celery) |
| [![Conda Recipe](https://img.shields.io/badge/recipe-airflow--with--cgroups-green.svg)](https://anaconda.org/conda-forge/airflow-with-cgroups) | [![Conda Downloads](https://img.shields.io/conda/dn/conda-forge/airflow-with-cgroups.svg)](https://anaconda.org/conda-forge/airflow-with-cgroups) | [![Conda Version](https://img.shields.io/conda/vn/conda-forge/airflow-with-cgroups.svg)](https://anaconda.org/conda-forge/airflow-with-cgroups) | [![Conda Platforms](https://img.shields.io/conda/pn/conda-forge/airflow-with-cgroups.svg)](https://anaconda.org/conda-forge/airflow-with-cgroups) |
| [![Conda Recipe](https://img.shields.io/badge/recipe-airflow--with--cloudant-green.svg)](https://anaconda.org/conda-forge/airflow-with-cloudant) | [![Conda Downloads](https://img.shields.io/conda/dn/conda-forge/airflow-with-cloudant.svg)](https://anaconda.org/conda-forge/airflow-with-cloudant) | [![Conda Version](https://img.shields.io/conda/vn/conda-forge/airflow-with-cloudant.svg)](https://anaconda.org/conda-forge/airflow-with-cloudant) | [![Conda Platforms](https://img.shields.io/conda/pn/conda-forge/airflow-with-cloudant.svg)](https://anaconda.org/conda-forge/airflow-with-cloudant) |
| [![Conda Recipe](https://img.shields.io/badge/recipe-airflow--with--crypto-green.svg)](https://anaconda.org/conda-forge/airflow-with-crypto) | [![Conda Downloads](https://img.shields.io/conda/dn/conda-forge/airflow-with-crypto.svg)](https://anaconda.org/conda-forge/airflow-with-crypto) | [![Conda Version](https://img.shields.io/conda/vn/conda-forge/airflow-with-crypto.svg)](https://anaconda.org/conda-forge/airflow-with-crypto) | [![Conda Platforms](https://img.shields.io/conda/pn/conda-forge/airflow-with-crypto.svg)](https://anaconda.org/conda-forge/airflow-with-crypto) |
| [![Conda Recipe](https://img.shields.io/badge/recipe-airflow--with--dask-green.svg)](https://anaconda.org/conda-forge/airflow-with-dask) | [![Conda Downloads](https://img.shields.io/conda/dn/conda-forge/airflow-with-dask.svg)](https://anaconda.org/conda-forge/airflow-with-dask) | [![Conda Version](https://img.shields.io/conda/vn/conda-forge/airflow-with-dask.svg)](https://anaconda.org/conda-forge/airflow-with-dask) | [![Conda Platforms](https://img.shields.io/conda/pn/conda-forge/airflow-with-dask.svg)](https://anaconda.org/conda-forge/airflow-with-dask) |
| [![Conda Recipe](https://img.shields.io/badge/recipe-airflow--with--databricks-green.svg)](https://anaconda.org/conda-forge/airflow-with-databricks) | [![Conda Downloads](https://img.shields.io/conda/dn/conda-forge/airflow-with-databricks.svg)](https://anaconda.org/conda-forge/airflow-with-databricks) | [![Conda Version](https://img.shields.io/conda/vn/conda-forge/airflow-with-databricks.svg)](https://anaconda.org/conda-forge/airflow-with-databricks) | [![Conda Platforms](https://img.shields.io/conda/pn/conda-forge/airflow-with-databricks.svg)](https://anaconda.org/conda-forge/airflow-with-databricks) |
| [![Conda Recipe](https://img.shields.io/badge/recipe-airflow--with--datadog-green.svg)](https://anaconda.org/conda-forge/airflow-with-datadog) | [![Conda Downloads](https://img.shields.io/conda/dn/conda-forge/airflow-with-datadog.svg)](https://anaconda.org/conda-forge/airflow-with-datadog) | [![Conda Version](https://img.shields.io/conda/vn/conda-forge/airflow-with-datadog.svg)](https://anaconda.org/conda-forge/airflow-with-datadog) | [![Conda Platforms](https://img.shields.io/conda/pn/conda-forge/airflow-with-datadog.svg)](https://anaconda.org/conda-forge/airflow-with-datadog) |
| [![Conda Recipe](https://img.shields.io/badge/recipe-airflow--with--docker-green.svg)](https://anaconda.org/conda-forge/airflow-with-docker) | [![Conda Downloads](https://img.shields.io/conda/dn/conda-forge/airflow-with-docker.svg)](https://anaconda.org/conda-forge/airflow-with-docker) | [![Conda Version](https://img.shields.io/conda/vn/conda-forge/airflow-with-docker.svg)](https://anaconda.org/conda-forge/airflow-with-docker) | [![Conda Platforms](https://img.shields.io/conda/pn/conda-forge/airflow-with-docker.svg)](https://anaconda.org/conda-forge/airflow-with-docker) |
| [![Conda Recipe](https://img.shields.io/badge/recipe-airflow--with--druid-green.svg)](https://anaconda.org/conda-forge/airflow-with-druid) | [![Conda Downloads](https://img.shields.io/conda/dn/conda-forge/airflow-with-druid.svg)](https://anaconda.org/conda-forge/airflow-with-druid) | [![Conda Version](https://img.shields.io/conda/vn/conda-forge/airflow-with-druid.svg)](https://anaconda.org/conda-forge/airflow-with-druid) | [![Conda Platforms](https://img.shields.io/conda/pn/conda-forge/airflow-with-druid.svg)](https://anaconda.org/conda-forge/airflow-with-druid) |
| [![Conda Recipe](https://img.shields.io/badge/recipe-airflow--with--elasticsearch-green.svg)](https://anaconda.org/conda-forge/airflow-with-elasticsearch) | [![Conda Downloads](https://img.shields.io/conda/dn/conda-forge/airflow-with-elasticsearch.svg)](https://anaconda.org/conda-forge/airflow-with-elasticsearch) | [![Conda Version](https://img.shields.io/conda/vn/conda-forge/airflow-with-elasticsearch.svg)](https://anaconda.org/conda-forge/airflow-with-elasticsearch) | [![Conda Platforms](https://img.shields.io/conda/pn/conda-forge/airflow-with-elasticsearch.svg)](https://anaconda.org/conda-forge/airflow-with-elasticsearch) |
| [![Conda Recipe](https://img.shields.io/badge/recipe-airflow--with--emr-green.svg)](https://anaconda.org/conda-forge/airflow-with-emr) | [![Conda Downloads](https://img.shields.io/conda/dn/conda-forge/airflow-with-emr.svg)](https://anaconda.org/conda-forge/airflow-with-emr) | [![Conda Version](https://img.shields.io/conda/vn/conda-forge/airflow-with-emr.svg)](https://anaconda.org/conda-forge/airflow-with-emr) | [![Conda Platforms](https://img.shields.io/conda/pn/conda-forge/airflow-with-emr.svg)](https://anaconda.org/conda-forge/airflow-with-emr) |
| [![Conda Recipe](https://img.shields.io/badge/recipe-airflow--with--github_enterprise-green.svg)](https://anaconda.org/conda-forge/airflow-with-github_enterprise) | [![Conda Downloads](https://img.shields.io/conda/dn/conda-forge/airflow-with-github_enterprise.svg)](https://anaconda.org/conda-forge/airflow-with-github_enterprise) | [![Conda Version](https://img.shields.io/conda/vn/conda-forge/airflow-with-github_enterprise.svg)](https://anaconda.org/conda-forge/airflow-with-github_enterprise) | [![Conda Platforms](https://img.shields.io/conda/pn/conda-forge/airflow-with-github_enterprise.svg)](https://anaconda.org/conda-forge/airflow-with-github_enterprise) |
| [![Conda Recipe](https://img.shields.io/badge/recipe-airflow--with--hdfs-green.svg)](https://anaconda.org/conda-forge/airflow-with-hdfs) | [![Conda Downloads](https://img.shields.io/conda/dn/conda-forge/airflow-with-hdfs.svg)](https://anaconda.org/conda-forge/airflow-with-hdfs) | [![Conda Version](https://img.shields.io/conda/vn/conda-forge/airflow-with-hdfs.svg)](https://anaconda.org/conda-forge/airflow-with-hdfs) | [![Conda Platforms](https://img.shields.io/conda/pn/conda-forge/airflow-with-hdfs.svg)](https://anaconda.org/conda-forge/airflow-with-hdfs) |
| [![Conda Recipe](https://img.shields.io/badge/recipe-airflow--with--jdbc-green.svg)](https://anaconda.org/conda-forge/airflow-with-jdbc) | [![Conda Downloads](https://img.shields.io/conda/dn/conda-forge/airflow-with-jdbc.svg)](https://anaconda.org/conda-forge/airflow-with-jdbc) | [![Conda Version](https://img.shields.io/conda/vn/conda-forge/airflow-with-jdbc.svg)](https://anaconda.org/conda-forge/airflow-with-jdbc) | [![Conda Platforms](https://img.shields.io/conda/pn/conda-forge/airflow-with-jdbc.svg)](https://anaconda.org/conda-forge/airflow-with-jdbc) |
| [![Conda Recipe](https://img.shields.io/badge/recipe-airflow--with--jenkins-green.svg)](https://anaconda.org/conda-forge/airflow-with-jenkins) | [![Conda Downloads](https://img.shields.io/conda/dn/conda-forge/airflow-with-jenkins.svg)](https://anaconda.org/conda-forge/airflow-with-jenkins) | [![Conda Version](https://img.shields.io/conda/vn/conda-forge/airflow-with-jenkins.svg)](https://anaconda.org/conda-forge/airflow-with-jenkins) | [![Conda Platforms](https://img.shields.io/conda/pn/conda-forge/airflow-with-jenkins.svg)](https://anaconda.org/conda-forge/airflow-with-jenkins) |
| [![Conda Recipe](https://img.shields.io/badge/recipe-airflow--with--jira-green.svg)](https://anaconda.org/conda-forge/airflow-with-jira) | [![Conda Downloads](https://img.shields.io/conda/dn/conda-forge/airflow-with-jira.svg)](https://anaconda.org/conda-forge/airflow-with-jira) | [![Conda Version](https://img.shields.io/conda/vn/conda-forge/airflow-with-jira.svg)](https://anaconda.org/conda-forge/airflow-with-jira) | [![Conda Platforms](https://img.shields.io/conda/pn/conda-forge/airflow-with-jira.svg)](https://anaconda.org/conda-forge/airflow-with-jira) |
| [![Conda Recipe](https://img.shields.io/badge/recipe-airflow--with--kubernetes-green.svg)](https://anaconda.org/conda-forge/airflow-with-kubernetes) | [![Conda Downloads](https://img.shields.io/conda/dn/conda-forge/airflow-with-kubernetes.svg)](https://anaconda.org/conda-forge/airflow-with-kubernetes) | [![Conda Version](https://img.shields.io/conda/vn/conda-forge/airflow-with-kubernetes.svg)](https://anaconda.org/conda-forge/airflow-with-kubernetes) | [![Conda Platforms](https://img.shields.io/conda/pn/conda-forge/airflow-with-kubernetes.svg)](https://anaconda.org/conda-forge/airflow-with-kubernetes) |
| [![Conda Recipe](https://img.shields.io/badge/recipe-airflow--with--ldap-green.svg)](https://anaconda.org/conda-forge/airflow-with-ldap) | [![Conda Downloads](https://img.shields.io/conda/dn/conda-forge/airflow-with-ldap.svg)](https://anaconda.org/conda-forge/airflow-with-ldap) | [![Conda Version](https://img.shields.io/conda/vn/conda-forge/airflow-with-ldap.svg)](https://anaconda.org/conda-forge/airflow-with-ldap) | [![Conda Platforms](https://img.shields.io/conda/pn/conda-forge/airflow-with-ldap.svg)](https://anaconda.org/conda-forge/airflow-with-ldap) |
| [![Conda Recipe](https://img.shields.io/badge/recipe-airflow--with--mongo-green.svg)](https://anaconda.org/conda-forge/airflow-with-mongo) | [![Conda Downloads](https://img.shields.io/conda/dn/conda-forge/airflow-with-mongo.svg)](https://anaconda.org/conda-forge/airflow-with-mongo) | [![Conda Version](https://img.shields.io/conda/vn/conda-forge/airflow-with-mongo.svg)](https://anaconda.org/conda-forge/airflow-with-mongo) | [![Conda Platforms](https://img.shields.io/conda/pn/conda-forge/airflow-with-mongo.svg)](https://anaconda.org/conda-forge/airflow-with-mongo) |
| [![Conda Recipe](https://img.shields.io/badge/recipe-airflow--with--mssql-green.svg)](https://anaconda.org/conda-forge/airflow-with-mssql) | [![Conda Downloads](https://img.shields.io/conda/dn/conda-forge/airflow-with-mssql.svg)](https://anaconda.org/conda-forge/airflow-with-mssql) | [![Conda Version](https://img.shields.io/conda/vn/conda-forge/airflow-with-mssql.svg)](https://anaconda.org/conda-forge/airflow-with-mssql) | [![Conda Platforms](https://img.shields.io/conda/pn/conda-forge/airflow-with-mssql.svg)](https://anaconda.org/conda-forge/airflow-with-mssql) |
| [![Conda Recipe](https://img.shields.io/badge/recipe-airflow--with--mysql-green.svg)](https://anaconda.org/conda-forge/airflow-with-mysql) | [![Conda Downloads](https://img.shields.io/conda/dn/conda-forge/airflow-with-mysql.svg)](https://anaconda.org/conda-forge/airflow-with-mysql) | [![Conda Version](https://img.shields.io/conda/vn/conda-forge/airflow-with-mysql.svg)](https://anaconda.org/conda-forge/airflow-with-mysql) | [![Conda Platforms](https://img.shields.io/conda/pn/conda-forge/airflow-with-mysql.svg)](https://anaconda.org/conda-forge/airflow-with-mysql) |
| [![Conda Recipe](https://img.shields.io/badge/recipe-airflow--with--password-green.svg)](https://anaconda.org/conda-forge/airflow-with-password) | [![Conda Downloads](https://img.shields.io/conda/dn/conda-forge/airflow-with-password.svg)](https://anaconda.org/conda-forge/airflow-with-password) | [![Conda Version](https://img.shields.io/conda/vn/conda-forge/airflow-with-password.svg)](https://anaconda.org/conda-forge/airflow-with-password) | [![Conda Platforms](https://img.shields.io/conda/pn/conda-forge/airflow-with-password.svg)](https://anaconda.org/conda-forge/airflow-with-password) |
| [![Conda Recipe](https://img.shields.io/badge/recipe-airflow--with--postgres-green.svg)](https://anaconda.org/conda-forge/airflow-with-postgres) | [![Conda Downloads](https://img.shields.io/conda/dn/conda-forge/airflow-with-postgres.svg)](https://anaconda.org/conda-forge/airflow-with-postgres) | [![Conda Version](https://img.shields.io/conda/vn/conda-forge/airflow-with-postgres.svg)](https://anaconda.org/conda-forge/airflow-with-postgres) | [![Conda Platforms](https://img.shields.io/conda/pn/conda-forge/airflow-with-postgres.svg)](https://anaconda.org/conda-forge/airflow-with-postgres) |
| [![Conda Recipe](https://img.shields.io/badge/recipe-airflow--with--qds-green.svg)](https://anaconda.org/conda-forge/airflow-with-qds) | [![Conda Downloads](https://img.shields.io/conda/dn/conda-forge/airflow-with-qds.svg)](https://anaconda.org/conda-forge/airflow-with-qds) | [![Conda Version](https://img.shields.io/conda/vn/conda-forge/airflow-with-qds.svg)](https://anaconda.org/conda-forge/airflow-with-qds) | [![Conda Platforms](https://img.shields.io/conda/pn/conda-forge/airflow-with-qds.svg)](https://anaconda.org/conda-forge/airflow-with-qds) |
| [![Conda Recipe](https://img.shields.io/badge/recipe-airflow--with--rabbitmq-green.svg)](https://anaconda.org/conda-forge/airflow-with-rabbitmq) | [![Conda Downloads](https://img.shields.io/conda/dn/conda-forge/airflow-with-rabbitmq.svg)](https://anaconda.org/conda-forge/airflow-with-rabbitmq) | [![Conda Version](https://img.shields.io/conda/vn/conda-forge/airflow-with-rabbitmq.svg)](https://anaconda.org/conda-forge/airflow-with-rabbitmq) | [![Conda Platforms](https://img.shields.io/conda/pn/conda-forge/airflow-with-rabbitmq.svg)](https://anaconda.org/conda-forge/airflow-with-rabbitmq) |
| [![Conda Recipe](https://img.shields.io/badge/recipe-airflow--with--redis-green.svg)](https://anaconda.org/conda-forge/airflow-with-redis) | [![Conda Downloads](https://img.shields.io/conda/dn/conda-forge/airflow-with-redis.svg)](https://anaconda.org/conda-forge/airflow-with-redis) | [![Conda Version](https://img.shields.io/conda/vn/conda-forge/airflow-with-redis.svg)](https://anaconda.org/conda-forge/airflow-with-redis) | [![Conda Platforms](https://img.shields.io/conda/pn/conda-forge/airflow-with-redis.svg)](https://anaconda.org/conda-forge/airflow-with-redis) |
| [![Conda Recipe](https://img.shields.io/badge/recipe-airflow--with--s3-green.svg)](https://anaconda.org/conda-forge/airflow-with-s3) | [![Conda Downloads](https://img.shields.io/conda/dn/conda-forge/airflow-with-s3.svg)](https://anaconda.org/conda-forge/airflow-with-s3) | [![Conda Version](https://img.shields.io/conda/vn/conda-forge/airflow-with-s3.svg)](https://anaconda.org/conda-forge/airflow-with-s3) | [![Conda Platforms](https://img.shields.io/conda/pn/conda-forge/airflow-with-s3.svg)](https://anaconda.org/conda-forge/airflow-with-s3) |
| [![Conda Recipe](https://img.shields.io/badge/recipe-airflow--with--salesforce-green.svg)](https://anaconda.org/conda-forge/airflow-with-salesforce) | [![Conda Downloads](https://img.shields.io/conda/dn/conda-forge/airflow-with-salesforce.svg)](https://anaconda.org/conda-forge/airflow-with-salesforce) | [![Conda Version](https://img.shields.io/conda/vn/conda-forge/airflow-with-salesforce.svg)](https://anaconda.org/conda-forge/airflow-with-salesforce) | [![Conda Platforms](https://img.shields.io/conda/pn/conda-forge/airflow-with-salesforce.svg)](https://anaconda.org/conda-forge/airflow-with-salesforce) |
| [![Conda Recipe](https://img.shields.io/badge/recipe-airflow--with--samba-green.svg)](https://anaconda.org/conda-forge/airflow-with-samba) | [![Conda Downloads](https://img.shields.io/conda/dn/conda-forge/airflow-with-samba.svg)](https://anaconda.org/conda-forge/airflow-with-samba) | [![Conda Version](https://img.shields.io/conda/vn/conda-forge/airflow-with-samba.svg)](https://anaconda.org/conda-forge/airflow-with-samba) | [![Conda Platforms](https://img.shields.io/conda/pn/conda-forge/airflow-with-samba.svg)](https://anaconda.org/conda-forge/airflow-with-samba) |
| [![Conda Recipe](https://img.shields.io/badge/recipe-airflow--with--sendgrid-green.svg)](https://anaconda.org/conda-forge/airflow-with-sendgrid) | [![Conda Downloads](https://img.shields.io/conda/dn/conda-forge/airflow-with-sendgrid.svg)](https://anaconda.org/conda-forge/airflow-with-sendgrid) | [![Conda Version](https://img.shields.io/conda/vn/conda-forge/airflow-with-sendgrid.svg)](https://anaconda.org/conda-forge/airflow-with-sendgrid) | [![Conda Platforms](https://img.shields.io/conda/pn/conda-forge/airflow-with-sendgrid.svg)](https://anaconda.org/conda-forge/airflow-with-sendgrid) |
| [![Conda Recipe](https://img.shields.io/badge/recipe-airflow--with--slack-green.svg)](https://anaconda.org/conda-forge/airflow-with-slack) | [![Conda Downloads](https://img.shields.io/conda/dn/conda-forge/airflow-with-slack.svg)](https://anaconda.org/conda-forge/airflow-with-slack) | [![Conda Version](https://img.shields.io/conda/vn/conda-forge/airflow-with-slack.svg)](https://anaconda.org/conda-forge/airflow-with-slack) | [![Conda Platforms](https://img.shields.io/conda/pn/conda-forge/airflow-with-slack.svg)](https://anaconda.org/conda-forge/airflow-with-slack) |
| [![Conda Recipe](https://img.shields.io/badge/recipe-airflow--with--ssh-green.svg)](https://anaconda.org/conda-forge/airflow-with-ssh) | [![Conda Downloads](https://img.shields.io/conda/dn/conda-forge/airflow-with-ssh.svg)](https://anaconda.org/conda-forge/airflow-with-ssh) | [![Conda Version](https://img.shields.io/conda/vn/conda-forge/airflow-with-ssh.svg)](https://anaconda.org/conda-forge/airflow-with-ssh) | [![Conda Platforms](https://img.shields.io/conda/pn/conda-forge/airflow-with-ssh.svg)](https://anaconda.org/conda-forge/airflow-with-ssh) |
| [![Conda Recipe](https://img.shields.io/badge/recipe-airflow--with--statsd-green.svg)](https://anaconda.org/conda-forge/airflow-with-statsd) | [![Conda Downloads](https://img.shields.io/conda/dn/conda-forge/airflow-with-statsd.svg)](https://anaconda.org/conda-forge/airflow-with-statsd) | [![Conda Version](https://img.shields.io/conda/vn/conda-forge/airflow-with-statsd.svg)](https://anaconda.org/conda-forge/airflow-with-statsd) | [![Conda Platforms](https://img.shields.io/conda/pn/conda-forge/airflow-with-statsd.svg)](https://anaconda.org/conda-forge/airflow-with-statsd) |
| [![Conda Recipe](https://img.shields.io/badge/recipe-airflow--with--vertica-green.svg)](https://anaconda.org/conda-forge/airflow-with-vertica) | [![Conda Downloads](https://img.shields.io/conda/dn/conda-forge/airflow-with-vertica.svg)](https://anaconda.org/conda-forge/airflow-with-vertica) | [![Conda Version](https://img.shields.io/conda/vn/conda-forge/airflow-with-vertica.svg)](https://anaconda.org/conda-forge/airflow-with-vertica) | [![Conda Platforms](https://img.shields.io/conda/pn/conda-forge/airflow-with-vertica.svg)](https://anaconda.org/conda-forge/airflow-with-vertica) |
| [![Conda Recipe](https://img.shields.io/badge/recipe-airflow--with--webhdfs-green.svg)](https://anaconda.org/conda-forge/airflow-with-webhdfs) | [![Conda Downloads](https://img.shields.io/conda/dn/conda-forge/airflow-with-webhdfs.svg)](https://anaconda.org/conda-forge/airflow-with-webhdfs) | [![Conda Version](https://img.shields.io/conda/vn/conda-forge/airflow-with-webhdfs.svg)](https://anaconda.org/conda-forge/airflow-with-webhdfs) | [![Conda Platforms](https://img.shields.io/conda/pn/conda-forge/airflow-with-webhdfs.svg)](https://anaconda.org/conda-forge/airflow-with-webhdfs) |
| [![Conda Recipe](https://img.shields.io/badge/recipe-airflow--with--winrm-green.svg)](https://anaconda.org/conda-forge/airflow-with-winrm) | [![Conda Downloads](https://img.shields.io/conda/dn/conda-forge/airflow-with-winrm.svg)](https://anaconda.org/conda-forge/airflow-with-winrm) | [![Conda Version](https://img.shields.io/conda/vn/conda-forge/airflow-with-winrm.svg)](https://anaconda.org/conda-forge/airflow-with-winrm) | [![Conda Platforms](https://img.shields.io/conda/pn/conda-forge/airflow-with-winrm.svg)](https://anaconda.org/conda-forge/airflow-with-winrm) |

Installing airflow-split
========================

Installing `airflow-split` from the `conda-forge` channel can be achieved by adding `conda-forge` to your channels with:

```
conda config --add channels conda-forge
```

Once the `conda-forge` channel has been enabled, `airflow, airflow-with-async, airflow-with-azure_blob_storage, airflow-with-cassandra, airflow-with-celery, airflow-with-cgroups, airflow-with-cloudant, airflow-with-crypto, airflow-with-dask, airflow-with-databricks, airflow-with-datadog, airflow-with-docker, airflow-with-druid, airflow-with-elasticsearch, airflow-with-emr, airflow-with-github_enterprise, airflow-with-hdfs, airflow-with-jdbc, airflow-with-jenkins, airflow-with-jira, airflow-with-kubernetes, airflow-with-ldap, airflow-with-mongo, airflow-with-mssql, airflow-with-mysql, airflow-with-password, airflow-with-postgres, airflow-with-qds, airflow-with-rabbitmq, airflow-with-redis, airflow-with-s3, airflow-with-salesforce, airflow-with-samba, airflow-with-sendgrid, airflow-with-slack, airflow-with-ssh, airflow-with-statsd, airflow-with-vertica, airflow-with-webhdfs, airflow-with-winrm` can be installed with:

```
conda install airflow airflow-with-async airflow-with-azure_blob_storage airflow-with-cassandra airflow-with-celery airflow-with-cgroups airflow-with-cloudant airflow-with-crypto airflow-with-dask airflow-with-databricks airflow-with-datadog airflow-with-docker airflow-with-druid airflow-with-elasticsearch airflow-with-emr airflow-with-github_enterprise airflow-with-hdfs airflow-with-jdbc airflow-with-jenkins airflow-with-jira airflow-with-kubernetes airflow-with-ldap airflow-with-mongo airflow-with-mssql airflow-with-mysql airflow-with-password airflow-with-postgres airflow-with-qds airflow-with-rabbitmq airflow-with-redis airflow-with-s3 airflow-with-salesforce airflow-with-samba airflow-with-sendgrid airflow-with-slack airflow-with-ssh airflow-with-statsd airflow-with-vertica airflow-with-webhdfs airflow-with-winrm
```

It is possible to list all of the versions of `airflow` available on your platform with:

```
conda search airflow --channel conda-forge
```


About conda-forge
=================

[![Powered by NumFOCUS](https://img.shields.io/badge/powered%20by-NumFOCUS-orange.svg?style=flat&colorA=E1523D&colorB=007D8A)](http://numfocus.org)

conda-forge is a community-led conda channel of installable packages.
In order to provide high-quality builds, the process has been automated into the
conda-forge GitHub organization. The conda-forge organization contains one repository
for each of the installable packages. Such a repository is known as a *feedstock*.

A feedstock is made up of a conda recipe (the instructions on what and how to build
the package) and the necessary configurations for automatic building using freely
available continuous integration services. Thanks to the awesome service provided by
[CircleCI](https://circleci.com/), [AppVeyor](https://www.appveyor.com/)
and [TravisCI](https://travis-ci.org/) it is possible to build and upload installable
packages to the [conda-forge](https://anaconda.org/conda-forge)
[Anaconda-Cloud](https://anaconda.org/) channel for Linux, Windows and OSX respectively.

To manage the continuous integration and simplify feedstock maintenance
[conda-smithy](https://github.com/conda-forge/conda-smithy) has been developed.
Using the ``conda-forge.yml`` within this repository, it is possible to re-render all of
this feedstock's supporting files (e.g. the CI configuration files) with ``conda smithy rerender``.

For more information please check the [conda-forge documentation](https://conda-forge.org/docs/).

Terminology
===========

**feedstock** - the conda recipe (raw material), supporting scripts and CI configuration.

**conda-smithy** - the tool which helps orchestrate the feedstock.
                   Its primary use is in the construction of the CI ``.yml`` files
                   and simplify the management of *many* feedstocks.

**conda-forge** - the place where the feedstock and smithy live and work to
                  produce the finished article (built conda distributions)


Updating airflow-split-feedstock
================================

If you would like to improve the airflow-split recipe or build a new
package version, please fork this repository and submit a PR. Upon submission,
your changes will be run on the appropriate platforms to give the reviewer an
opportunity to confirm that the changes result in a successful build. Once
merged, the recipe will be re-built and uploaded automatically to the
`conda-forge` channel, whereupon the built conda packages will be available for
everybody to install and use from the `conda-forge` channel.
Note that all branches in the conda-forge/airflow-split-feedstock are
immediately built and any created packages are uploaded, so PRs should be based
on branches in forks and branches in the main repository should only be used to
build distinct package versions.

In order to produce a uniquely identifiable distribution:
 * If the version of a package **is not** being increased, please add or increase
   the [``build/number``](https://conda.io/docs/user-guide/tasks/build-packages/define-metadata.html#build-number-and-string).
 * If the version of a package **is** being increased, please remember to return
   the [``build/number``](https://conda.io/docs/user-guide/tasks/build-packages/define-metadata.html#build-number-and-string)
   back to 0.

Feedstock Maintainers
=====================

* [@halldc](https://github.com/halldc/)
* [@sodre](https://github.com/sodre/)

