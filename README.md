# awsiplistkql

**awsiplistkql** simplifies and flattens AWS's public IP ranges into a JSON format that is compatible with the `externaldata` operator in KQL.

> The native AWS IP ranges JSON (https://ip-ranges.amazonaws.com/ip-ranges.json) contains a nested structure that does **not** work well with `externaldata`.  
> This tool converts it into a clean, one-line object with just the required IP CIDRs.

