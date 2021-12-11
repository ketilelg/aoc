#!/usr/bin/perl
use List::Util qw(min max);
use strict;

my @map;
my $w=0;
my $h=0;
while (<>) #les inn kartet.
{
    chomp;
    $w=0;
    foreach $b (split //)
    {
	$map[$h][$w]=$b;
	$w++;
    }
    $h++;
}

my $flashes=0;

sub gen
{
    #først: øk med en:
    for my $y (0..$h-1)
    {
	for my $x (0..$w-1)
	{
	    $map[$y][$x]+=1;
	}
    }

    my @fmap;
    my $oflashes=-1;
    while($oflashes!=$flashes)
    {
	$oflashes=$flashes;
	#så, gå gjennom alle
	for my $y (0..$h-1)
	{
	    for my $x (0..$w-1)
	    {
		if (($map[$y][$x] > 9) && !$fmap[$y][$x]) #har ikke flasjet, så flash, denne omgang
		{
		    $fmap[$y][$x]=1;
		    $flashes++;
		    for my $rx (max(0,$x-1)..min($x+1,$w-1))
		    {
			for my $ry (max(0,$y-1)..min($y+1,$h-1))
			{
			    $map[$ry][$rx]++;
			}
		    }
		}	    
	    }
	}
    }

    for my $y (0..$h-1)
    {
	for my $x (0..$w-1)
	{
	    if($map[$y][$x] > 9)
	    {
		$map[$y][$x] = 0;
	    }
	}
    }

    
#    for my $y (0..$h-1)
#    {
#	print "$y ";
#	for my $x (0..$w-1)
#	{
#	    print "$map[$y][$x]";	    
#	}
#	print "\n";
#    }

    
}

for my $gen (1..100)
{
    gen;
}
    print "part1: $flashes\n";


my $gens=100;
$flashes=0;
while ($flashes < 100)
{
    $flashes=0;
    gen;
    $gens++

}

print "part2: $gens\n";
