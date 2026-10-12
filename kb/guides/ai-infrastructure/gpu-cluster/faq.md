# FAQ (FPT Cloud docs)

> Nguồn: https://docs.fptcloud.com/docs/ai-infrastructure/gpu-cluster/faq/

# FAQ

## Regional availability​

GPU Cluster operates in 4 regions: Hanoi, Ho Chi Minh City, Hoa Lac, and Japan. Clusters running across multiple regions are not supported.

## Cluster configuration​

The platform allows multiple VM configurations within a single cluster using Worker Groups. Default limits are 100 Worker nodes per group and 100 Worker groups per cluster.

## Compatibility​

GPU Cluster is fully compatible with Kubernetes platforms on other clouds such as AWS, Azure, GCP, and DigitalOcean, enabling straightforward application migration.

## Scaling behavior​

The Cluster Autoscaler operates on resource demands (CPU and memory) of the pods deployed on nodes, not actual resource usage. It adds nodes when pods queue due to insufficient resources and removes underutilized nodes after 30 minutes.

## Known limitations​

  * Worker Group configurations cannot be modified directly — you must create a new Worker Group instead.
  * Cluster upgrades follow a rolling mechanism but may cause temporary downtime.
  * Taints are not supported at the Worker Group level.
  * A non-deletable "worker group base" maintains system components and cannot be removed.
