import time
import argparse
from solana.rpc.api import Client

def get_block_height(rpc_url, sleep_time_ms, num_iterations):
    client = Client(rpc_url)

    execution_times = []

    for i in range(num_iterations):
        start_time = time.time()

        client.get_block_height()
        # print(client.get_cluster_nodes())

        end_time = time.time()
        execution_time_ms = (end_time - start_time) * 1000  # Convert to milliseconds
        execution_times.append(execution_time_ms)

        # Display execution time of each iteration
        print(f"Time elapsed: {execution_time_ms:.3f} ms")

        time.sleep(sleep_time_ms / 1000)  # Convert sleep time to seconds

    return execution_times

def main():
    parser = argparse.ArgumentParser(description='Measure execution time of Solana RPC calls.')

    parser.add_argument('-u','--rpc_url', type=str, default='https://api.mainnet-beta.solana.com', help='RPC URL')
    parser.add_argument('-s','--sleep', type=float, default=50, help='Sleep time in milliseconds between iterations (default: 50)')
    parser.add_argument('-i','--iterations', type=int, default=10, help='Number of iterations (default: 10)')

    args = parser.parse_args()

    print(f"RPC URL: {args.rpc_url}")
    print(f"Sleep time: {args.sleep} milliseconds")
    print(f"Number of iterations: {args.iterations}")

    execution_times = get_block_height(args.rpc_url, args.sleep / 1000, args.iterations)

    total_time = sum(execution_times)
    avg_execution_time = total_time / args.iterations

    print(f"Average Execution Time: {avg_execution_time:.3f} ms")

if __name__ == "__main__":
    main()
