import pyarrow.parquet as pq

table = pq.read_table("data/benchmark.parquet")
series = table["series"][0].as_py()
true_cps = table["changepoints"][0].as_py()

detected_cps = pelt(np.array(series), penalty=10.0)

print("true changepoints:", true_cps)
print("detected changepoints:", detected_cps)
