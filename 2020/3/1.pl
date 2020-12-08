#!/opt/local/bin/perl
my $lno=0;
while(<>)
{
chomp;
my $len = length $_;

my $c1=substr $_,($lno*1) % $len,1;
if(($c1 eq "#"))
{print "jepp1.\n"}

my $c1=substr $_,($lno*3) % $len,1;
if(($c1 eq "#"))
{print "jepp2.\n"}

my $c1=substr $_,($lno*5) % $len,1;
if(($c1 eq "#"))
{print "jepp3.\n"}

my $c1=substr $_,($lno*7) % $len,1;
if(($c1 eq "#"))
{print "jepp4.\n"}

if($lno % 2 == 0)
{
my $c1=substr $_,($lno/2) % $len,1;
if(($c1 eq "#"))
{print "jepp5.\n"}
}
$lno++;
}
