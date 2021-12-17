#!/usr/bin/perl

use List::Util qw(min max);

$s=<>;

$s=~/target area: x=(-?\d+)..(-?\d+), y=(-?\d+)..(-?\d+)/;

print "$1,$2,$3,$4\n";

$minx=min($1,$2);
$maxx=max($1,$2);
$miny=min($3,$4);
$maxy=max($3,$4);

my $ddy=1;
if ($minx < 0) { $ddx=-1; } else {$ddx=1;}

my $dx=0;
my $dy=0;
my $hh=$miny;
for my $dx (0..abs($maxx))
{
    for my $dy(-abs($miny)..abs($miny))
    {
	my $x=0;
	my $y=0;
	my $mdx=$dx;
	my $mdy=$dy;
	my $h=$miny-1;
	while(($x<=$maxx) && ($y>=$miny))
	{
	    $x+=$mdx;
	    $y+=$mdy;
	    if($y>$h){$h=$y;}
	    print "l: $dx $dy $x $y $h";
	    if(($x>=$minx)&&($x<=$maxx)&&($y>=$miny)&&($y<=$maxy))
	    {
		print "treff!\n";
		if ($h>$hh)
		{
		    $hh=$h;
		}
		break;
	    }
	    print "\n";
	    if($mdx>0){$mdx--;}
	    $mdy--;
	}
	print "$dx $dy $mdx $mdy $x $y\n";
    }
}

print "p1: $hh\n";

# part 2 løsning:
#  ./1.pl input | grep treff | cut -d" " -f 2,3 | sort | uniq | wc -l
