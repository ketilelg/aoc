#!/usr/bin/perl

use List::Util qw(min max);

my $pt = <>;
chomp $pt;

my %pir;

while (<>)
{
    if (/(\w\w) -> (\w)/ )
    {
	$pir{$1} = $2;
    }
}

for my $i (1..10)
{
    my $sc="!";
    my $npt="";
    my $lc;
    for my $c (split //, $pt)
    {
	if ($pir{$sc.$c})
	{
	    $npt = $npt . $sc . $pir{$sc.$c};
	}
	$sc=$c;
    }
    $pt=$npt.$sc;
}

my %count;
for my $c (split //, $pt)
{
    $count{$c}++;
}

my $diff=max (values %count) - min (values %count);

print "part1: $diff\n";
