#!/bin/bash
source .env

# 获取当前IPv6地址
current_ipv6=$(curl -s https://6.ipw.cn/)

# 获取当前IPv4地址
current_ipv4=$(curl -s https://4.ipw.cn/)


# 更新IPv6记录
curl -X PUT -H "X-Auth-Email: $USER_EMAIL" \
         -H "X-Auth-Key: $API_KEY" \
         -H "Content-Type: application/json" \
         -d '{"type":"AAAA","name":"'"$RECORD_NAME"'","content":"'"$current_ipv6"'"}' \
         "https://api.cloudflare.com/client/v4/zones/$ZONE_ID/dns_records/$AAAA_RECORD_ID"

# 更新IPv4记录
curl -X PUT -H "X-Auth-Email: $USER_EMAIL" \
         -H "X-Auth-Key: $API_KEY" \
         -H "Content-Type: application/json" \
         -d '{"type":"A","name":"'"$RECORD_NAME"'","content":"'"$current_ipv4"'"}' \
         "https://api.cloudflare.com/client/v4/zones/$ZONE_ID/dns_records/$A_RECORD_ID"
