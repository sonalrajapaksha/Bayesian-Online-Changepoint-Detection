import matplotlib.pyplot as plt
import pyarrow.parquet as pq

table = pq.read_table("data/benchmark.parquet")

fig, axes = plt.subplots(3, 1, figsize=(12, 8))

for i, ax in enumerate(axes):
    series = table["series"][i].as_py()
    changepoints = table["changepoints"][i].as_py()

    ax.plot(series, color="steelblue", linewidth=0.8)

    for cp in changepoints:
        ax.axvline(
            x=cp,
            color="red",
            linestyle="--",
            linewidth=1.2,
            label="changepoint" if cp == changepoints[0] else "",
        )

    ax.set_title(f"series {i} — changepoints at {changepoints}")
    ax.legend(loc="upper right")

plt.tight_layout()
plt.savefig("data/sample_series.png")
plt.show()
