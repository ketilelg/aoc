#!/opt/local/bin/perl

use strict;

my $pk = 1614360;
#my $pk = 5764801;
my $sn = 1;
my $loop = 0;

while($sn != $pk)
{
    $sn = $sn * 7;
    $sn = $sn % 20201227;
    $loop++;

}
print "loop: $loop $sn\n";
my $cpk=$sn;
my $pk = 7734663;
#my $pk = 17807724;
my $sn = 1;
my $loop = 0;

while($sn != $pk)
{
    $sn = $sn * 7;
    $sn = $sn % 20201227;
    $loop++;

}
print "loop: $loop $sn\n\n";

$sn=1;
#$loop++;
while ($loop)
{

    $sn = $sn * $cpk;
    $sn = $sn % 20201227;
        $loop--;

}
    print "loop: $loop $sn\n";


