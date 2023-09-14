import os
import subprocess
from pyfiglet import Figlet

def run_command(command, output_file=None):
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
    output, error = process.communicate()
    
    if output_file:
        with open(output_file, 'w') as file:
            file.write(output.decode('utf-8'))
    
    return output.decode('utf-8').split('\n')

def recon(target):
    f = Figlet(font='slant')
    print(f.renderText('Recon Script'))
    
    print(f"Running recon on: {target}\n")

    print("Finding subdomains with Subfinder...\n")
    subdomains = run_command(f"subfinder -d {target} -silent", "subdomains777.txt")
    for subdomain in subdomains:
        print(subdomain)

    print("Finding assets with assetfinder...\n")
    assets = run_command(f"assetfinder -subs-only {target}", "assets777.txt")
    for asset in assets:
        print(asset)

    print("Finding subdomains with findomain...\n")
    findomains = run_command(f"findomain -t {target} | tail -n +13 | head -n -4", "findomains777.txt")
    for findomain in findomains:
        print(findomain)

    run_command(f"cat assets777.txt findomains777.txt subdomains777.txt >> main777.txt")

    uniq = run_command(f"sort main777.txt | uniq -i > domain777.txt")

    print("Running httpx...\n")
    httpx_result = run_command(f"httpx-toolkit -l domain777.txt -sc 200 -mc'200, 300'", "httpx_results.txt")
    for result in httpx_result:
        print(result)

    print(" THANK YOU \n")
    dell = run_command(f"rm -rf domain777.txt assets777.txt findomains777.txt subdomains777.txt main777.txt")


if __name__ == "__main__":
    target = input("Enter the target for scan: ")
    recon(target)
