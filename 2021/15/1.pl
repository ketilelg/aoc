#!/usr/bin/perl

use List::Util qw(min max);


my @dmap;

my $w;
my $line=0;
while(<>)
{
    $w=length;
    my @lc=split//;
    for my $c (0..$#lc)
    {
	$dmap[$line][$c]=$lc[$c];
    }

    $line++;
}
$line--;
$w--;
$w--;

for my $y (0..$line)
{
    for my $x (0..$w)
    {
       print "$dmap[$y][$x]";
    
    }
    print "\n";
}

my @rmap; # risk from 0,0

sub rr
{ #recurse, x y, cost as input.
    my $x=$_[0];
    my $y=$_[1];
    my $c=$_[2];

    my $r=$c+$dmap[$y][$x];
    $rmap[$y][$x]=$r;
#    print "rr: $x $y $r\n";
    if (($x > 0)) #vi kan se til venstre
    {
	if ((! defined $rmap[$y][$x-1]))
	{
	    rr($x-1,$y,$r);
	}
    }
    if (($y > 0)) #vi kan se opp
    {
	if ((! defined $rmap[$y-1][$x]))
	{
	    rr($x,$y-1,$r);
	}
    }
    if (($x < $w)) #vi kan se til høyre
    {
	if ((! defined $rmap[$y][$x+1]))
	{
	    rr($x+1,$y,$r);
	}
    }
    if (($y < $line)) #vi kan se ned
    {
	if ((! defined $rmap[$y+1][$x]))
	{
	    rr($x,$y+1,$r);
	}
    }
}

rr(0,0,0);

for my $y (0..$line)
{
    for my $x (0..$w)
    {
       print "$rmap[$y][$x]-";
    
    }
    print "\n";
}
