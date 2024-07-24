from prefect import flow


@flow(log_prints=True)
def my_flow(name: str = "World"):
    print(f"Hello {name}!")


if __name__ == "__main__":
    my_flow.from_source().deploy(
        name="pacc-deployment-process-1",
        work_pool_name="pacc-process-pool",
        tags=["pacc", "hello"],
    )
