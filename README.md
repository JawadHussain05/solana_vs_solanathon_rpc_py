# solana_vs_solanathon_rpc_py
This is a simple repository aimed at benchmarking solana-sdk library and solathon library.
It is written in python3 and are working on the solana mainnet endpoint but it can be changed

## HOW TO RUN
To run simply follow the following steps
```
python3 ./rpc_client_solana.py -i <no._of_iterations> -s <sleep_time_between_iterations> -u <url_or_endpoint>

python3 ./rpc_client_solathon.py -i <no._of_iterations> -s <sleep_time_between_iterations> -u <url_or_endpoint>
```
## NOTE:
Default values are
-i = 10
-s = 50
-u = https://api.mainnet-beta.solana.com

for best results take tests with at least 500 iterations

## Results
solathon shows less latency

##Improvements:
replace the httpx library used with requests for better performance but it will result in no async mode
