#!/opt/local/bin/perl
my $low=1000;
my $high=0;
while(<>)
{
chomp;
print "linje: ´$_´\n";

my $row=0;
my $brb=64;
for my $i (0..6)
{
my $c=substr $_,$i,1;
print "i: $i c: $c\n";
if($c eq "B") { $row += $brb; }
$brb=$brb/2;
}
my $seat=0;
my $sr=4;
for my $i (0..2)
{
my $c=substr $_,$i+7,1;
print "i: $i c: $c\n";
if($c eq "R") { $seat += $sr; }
$sr=$sr/2;
}

s/F/0/g;
s/B/1/g;
s/R/1/g;
s/L/0/g;
print "binary: $_\n";
$bsid = oct("0b" . $_);
$sid=$row*8 + $seat;
print "row: $row\nseat: $seat\n$sid seatid bsid: $bsid\n";
if ($sid < $low ) { $low = $sid; }
if ($sid > $high ) { $high = $sid; }
$seats[$bsid]="taken";
}
for my $i ($low..$high)
{
print "seat $i is $seats[$i]\n";
}
