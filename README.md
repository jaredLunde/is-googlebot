# is-googlebot
Tests whether or not an IP/User-Agent pair is actually Googlebot.
First this library will test the User-Agent to see if it matches known
Googlebot UAs. If it doesn't, it returns `False` right away to 
quickly bailout. If it does match, it will check the DNS hostname of the
IP against known Googlebot hostnames. If it isn't spoofed, it will return
`True`. This is the only way to safely test whether or not a given bot is 
actually Googlebot.

## Installation
`poetry add is-googlebot`
or
`pip install is-googlebot`

## Usage
```python
import is_googlebot

is_googlebot.test(ip_address, user_agent)  # user_agent is optional, an IP alone can be tested
# True if this is Googlebot
```
