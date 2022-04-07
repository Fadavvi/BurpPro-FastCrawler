# BurpPro-FastCrawler
the simplest way to integrate your subdomain enum outputs with Burp Pro (With Fast Crawler option)

Burp Pro Fast Crawler

# Arguments:
  ```
  -h, --help            show this help message and exit
  -f FILE, --file FILE  List of domains/subdoamins
  -i IP, --ip IP        IP addr of Burp API (Default: 127.0.0.1)
  -p PORT, --port PORT  Port of Burp API (Default: 1337)
  -k KEY, --key KEY     Burp API Key
  ```

# Usage:
```
python3 burp-int.py -f <PathToList.txt> -k <BurpAPIKey>
```

# Note: 
I strongly advise you to set your scope(s) in Burp before running the script.
