if [ "$#" != "1" ];
then
  echo "Usage: $0 <pid>"
  exit
fi

pid=$1
export LC_NUMERIC="en_US.UTF-8" # printf would complain otherwise
while [ -e /proc/$pid ];
do
  mem=$(pmap $pid | grep "total" | sed "s|  *| |g" | cut -d " " -f 3 | sed "s|K||g")
  mem_in_gb=$(echo "$mem / (1024 * 1024)" | bc -l)
  mem_in_gb=0$mem_in_gb
  printf "%0.2fG\n" $mem_in_gb
  sleep 1
done
