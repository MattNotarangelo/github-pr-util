# Github pull requests

## ROKT/kafka-configs

Pull request|Impact
---|---
[NO-JIRA Add cue validation](https://github.com/ROKT/kafka-configs/pull/764)|BAU: Kafka topic resiliency
[NO-JIRA: Add `helm.sh/resource-policy: keep` to KafkaTopics](https://github.com/ROKT/kafka-configs/pull/755)|Improvement: Prevent accidental deletion of topic CRs
[DMR-732: [PROD] Mn/setup all mirrors](https://github.com/ROKT/kafka-configs/pull/743)|BAU: LDR mirroring architecture design
[NO-JIRA: Refactor kafka configs pipelines](https://github.com/ROKT/kafka-configs/pull/736)|Improvement: reduced LOC by 65%
[NO-JIRA: Make deployment faster](https://github.com/ROKT/kafka-configs/pull/728)|Improvement: Sped up kafka topic deployment by 70% [results](https://docs.google.com/spreadsheets/d/1NFyTCSDqUcR30HHaWodoCtF_5YEe3N-Qo4JA29kbq04/edit?usp=sharing)

## ROKT/kafka

Pull request|Impact
---|---
[NO-JIRA: Script to generate EBS usage by topic](https://github.com/ROKT/kafka/pull/244)|Improvement: track EBS usage to optimise replication factor and retention
[NO-JIRA: Block image builds](https://github.com/ROKT/kafka/pull/232)|Improvement: Prevent unnecessary kafka image builds
[NO-JIRA: Stop SR diff every time](https://github.com/ROKT/kafka/pull/224)|Improvement: Prevent unnecessary redeployment of schema registry pods causing errors to be returned to clients
[NO-JIRA: Refactor mm2 helm config](https://github.com/ROKT/kafka/pull/222)|Improvement: Reduced size and complexity of MM2 helm values by using standardised config. Reduced LOC by 70%
[DMR-715: Deploy kafka components in all regions [PROD]](https://github.com/ROKT/kafka/pull/220)|Feat: Kafka data residency changes
[NO-JIRA: Refactor kafka pipeline](https://github.com/ROKT/kafka/pull/219)|Improvement: Reduced Kafka BK pipeline LOC by 60%, improved readability
[NO-JIRA: enable compression for eu and ue mm2](https://github.com/ROKT/kafka/pull/212)|Improvement: Enable MM2 compression to reduce cross-az data transfer costs (est. savings = $30k/yr)
[NO-JIRA: Enable auto.leader.rebalance](https://github.com/ROKT/kafka/pull/185)|Improvement: Eliminate the need for manual leader election
[DMR-540: Upgrade kafka to 3.5 [stage 3]](https://github.com/ROKT/kafka/pull/184)|BAU: Kafka upgrades
[DMR-263: Eliminate cross region image pull](https://github.com/ROKT/kafka/pull/183)|Improvement: Stop kafka cross region image pulls for faster deployment
[NO-JIRA: reduce deployment time 2](https://github.com/ROKT/kafka/pull/164)|Improvement: Reduce Kafka deployment time by 40s per broker (10%)
[DMR-508: Improve Kafka deployment speed](https://github.com/ROKT/kafka/pull/154)|Improvement: Reduce Kafka deployment time by 50% [results](https://rokt.atlassian.net/wiki/spaces/~63b14f2ef3e7004f77fdc38b/pages/2763128866/Kafka+deployment+speedup)
[NO-JIRA: Reduce StrimziPodSet CR size](https://github.com/ROKT/kafka/pull/153)|Fix: hotfix to reduce StrimziPodSet CR size

## ROKT/kafka-connect

Pull request|Impact
---|---
[NO-JIRA: stop connect diff every build](https://github.com/ROKT/kafka-connect/pull/144)|Improvement: Stop kafka-connect pods from rolling on each deployment
[Dmr 715 deploy kafka components in all regions](https://github.com/ROKT/kafka-connect/pull/135)|BAU: Kafka data residency changes
[DMR-524: Move kafka connect to ARM](https://github.com/ROKT/kafka-connect/pull/117)|BAU: Run kafka connect on ARM arch
[DMR-527: Upgrade kafka connect versions](https://github.com/ROKT/kafka-connect/pull/110)|BAU: Kafka connect version upgrades
[NO-JIRA: pull rokt-kube-cli from correct region](https://github.com/ROKT/kafka-connect/pull/108)|Improvement: Reduce cross region image pulls

## ROKT/spark-infra

Pull request|Impact
---|---
[Dmr 702 spark provision eu west 1 region](https://github.com/ROKT/spark-infra/pull/172)|BAU: Deploy spark in eu-west-1

## ROKT/spark-examples

Pull request|Impact
---|---
[DMR-657: Spark add e2e test to demo batch application](https://github.com/ROKT/spark-examples/pull/11)|BAU: Add spark E2E test
[DMR-654: Spark build a demo batch applications](https://github.com/ROKT/spark-examples/pull/10)|BAU: Spark demo batch application

## ROKT/spark-on-k8s-operator

Pull request|Impact
---|---
[DMR-624: Prevent webhook from being deleted when pods are deleted](https://github.com/ROKT/spark-on-k8s-operator/pull/23)|BAU: Resolve downtime during deployments
[DMR-615: Spark add support for nvme spill volumes](https://github.com/ROKT/spark-on-k8s-operator/pull/21)|BAU: Add support for NVMe spill volumes

## ROKT/flipt

Pull request|Impact
---|---
[NO-JIRA: Add quitquitquit endpoint](https://github.com/ROKT/flipt/pull/254)|Improvement: enable flipt sidecar use with cronjob
[DMR-463: Move flipt sidecar injector to service arm](https://github.com/ROKT/flipt/pull/240)|BAU: Move flipt sidecar injector to ARM arch
[NO-JIRA: fix flipt database issues](https://github.com/ROKT/flipt/pull/237)|Fix: Fix flipt DB connection issues
[DMR-248: Flipt create operations playbook](https://github.com/ROKT/flipt/pull/232)|BAU: Flipt playbook
[DMR-206: Update Flipt to v1.20](https://github.com/ROKT/flipt/pull/220)|BAU: Flipt version upgrades
[NO-JIRA: Implement sidecar retry](https://github.com/ROKT/flipt/pull/216)|Improvement: Add flipt sidecar retry logic
[DMR-180: Deploy Flipt RDS Replica to all regions](https://github.com/ROKT/flipt/pull/212)|BAU: Flipt arch design
[Dmr 125 setup single portal v2](https://github.com/ROKT/flipt/pull/209)|BAU: Flipt arch design
[Dmr 139 flipt add unit tests mocking for sidecar](https://github.com/ROKT/flipt/pull/208)|BAU: Flipt sidecar testing
[DMR-135: Flipt add caching for evaluate/batchevaluate](https://github.com/ROKT/flipt/pull/198)|BAU: Implement evaluate caching in flipt sidecar
[DMR-42: Flipt audit logging](https://github.com/ROKT/flipt/pull/174)|BAU: Flipt audit logging

## ROKT/aws-eks

Pull request|Impact
---|---
[DMR-615: Add support for nvme spill volumes [prod]](https://github.com/ROKT/aws-eks/pull/1252)|BAU: Add support for NVMe spill volumes

## ROKT/finance-and-accounts

Pull request|Impact
---|---
[[NO-JIRA]: Refactor flipt-daemon infra to use sidecar injector label](https://github.com/ROKT/finance-and-accounts/pull/428)|BAU: Cross-service flipt migration

## ROKT/ads-api

Pull request|Impact
---|---
[[NO-JIRA]: Replace flipt-daemon infra with sidecar-injector](https://github.com/ROKT/ads-api/pull/292)|BAU: Cross-service flipt migration

## ROKT/op2-workspace

Pull request|Impact
---|---
[[NO-JIRA]: Refactor/Replace flipt-daemon infra with sidecar-injector](https://github.com/ROKT/op2-workspace/pull/2258)|BAU: Cross-service flipt migration

## ROKT/rokt-transactions

Pull request|Impact
---|---
[NO-JIRA: [Refactor] Replace flipt-daemon infra with sidecar-injector](https://github.com/ROKT/rokt-transactions/pull/537)|BAU: Cross-service flipt migration

## ROKT/rokt-consumer-attributes-processor

Pull request|Impact
---|---
[CDP-xxx: increase kafka producer batch size](https://github.com/ROKT/rokt-consumer-attributes-processor/pull/136)|Improvement: Enable batch producing to kafka. Result: xxx

## ROKT/organization

Pull request|Impact
---|---
[DE-573: Generate aws tag policy based off rokt organisation evaluation mode only](https://github.com/ROKT/organization/pull/57)|BAU: setup tag policy from rokt-organisation

