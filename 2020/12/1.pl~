#!/opt/local/bin/perl

while(<>)
{
/(\d+)-(\d+)\s(\w):\s(\w+)/;
$p1=$1;
$p2=$2;
$c1=substr $4,$p1-1,1;
$c2=substr $4,$p2-1,1;
print "1: .$1. .2: .$2. 3: .$3. 4:.$4. c1: .$c1. c2: .$c2.\n";

# if(($c2 eq $c1))
# {print "jeppx.\n"}

if(($c2 ne $3) && ($c1 eq $3))
{print "jepp1.\n"}
if(($c1 ne $3) && ($c2 eq $3))
{print "jepp2.\n"}k
}
