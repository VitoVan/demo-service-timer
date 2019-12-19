while { echo -en "HTTP/1.1 200 OK\r\nConnection: keep-alive\r\n\r\n$(date +'%Y-%m-%d %T') @ $(ifconfig eth0 | grep 'inet addr' | cut -d: -f2 | awk '{print $1}')\r\n"; } | nc -l -s 0.0.0.0 -p 80; do
  echo "================================================"
done
