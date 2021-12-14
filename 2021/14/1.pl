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

for my $i (1..20)
{
    my $sc="!";
    my $npt="";
    my $lc;
    for my $c (split //, $pt)
    {
#	print "c: $c $pir{$sc.$c} \n ";
	if ($pir{$sc.$c})
	{
	    $npt = $npt . $sc . $pir{$sc.$c};
#	    print "npt: $npt\n";t
	}
	$sc=$c;

#	print "c: $c\n";
    }

    $pt=$npt.$sc;
    print "runde $i\n";
}

my %count;
for my $c (split //, $pt)
{
    $count{$c}++;
}

print "\n";

my $diff=max (values %count) - min (values %count);

for my $c (keys(%count))
{
    print "$c: $count{$c}\n"
}

print "part1: $diff\n";
