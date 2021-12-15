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
{ #recurse, x y, cost, depth as input.
    my $x=$_[0];
    my $y=$_[1];
    my $c=$_[2];
    my $rd=$_[3];

    if ($rd > 0)
    {
	my $r=$c+$dmap[$y][$x];
	$rmap[$y][$x]=$r;
	    print "rrb: $x $y $r $rd\n";
	if (($x > 0)) #vi kan se til venstre
	{
	    if ((! defined $rmap[$y][$x-1]))
	    {
		rr($x-1,$y,$r,$rd-1);
	    }
	    else
	    {
		if($rmap[$y][$x-1]+$dmap[$y][$x] < $rmap[$y][$x])
		{
		    $rmap[$y][$x]=$rmap[$y][$x-1]+$dmap[$y][$x];
		}
	    }
	}
	if (($y > 0)) #vi kan se opp
	{
	    if ((! defined $rmap[$y-1][$x]))
	    {
		rr($x,$y-1,$r,$rd-1);
	    }
	    else
	    {
		if($rmap[$y-1][$x]+$dmap[$y][$x] < $rmap[$y][$x])
		{
		    $rmap[$y][$x]=$rmap[$y-1][$x]+$dmap[$y][$x];
		}
	    }
	}
	if (($x < $w)) #vi kan se til høyre
	{
	    if ((! defined $rmap[$y][$x+1]))
	    {
		rr($x+1,$y,$r,$rd-1);
	    }
	    else
	    {
		if($rmap[$y][$x+1]+$dmap[$y][$x] < $rmap[$y][$x])
		{
		    $rmap[$y][$x]=$rmap[$y][$x+1]+$dmap[$y][$x];
		}
	    }
	}
	if (($y < $line)) #vi kan se ned
	{
	    if ((! defined $rmap[$y+1][$x]))
	    {
		rr($x,$y+1,$r,$rd-1);
	    }
	    else
	    {
		if($rmap[$y+1][$x]+$dmap[$y][$x] < $rmap[$y][$x])
		{
		    $rmap[$y][$x]=$rmap[$y+1][$x]+$dmap[$y][$x];
		}
	    }
	}
    }
    print "rr: $x- $y- $r- $rd\n";
}

$rmap[0][0]=0;
rr(0,0,0,200);

#iterer, se alltid til v/opp, avhengig av hva som går. 
sub naive
{
    $rmap[0][0]=0;
    for my $y (0..$line)
    {
	for my $x (0..$w)
	{
	    if($y > 0)
	    {
		if($x>0)
		{
		    $rmap[$y][$x] = $dmap[$y][$x] + min($rmap[$y][$x-1],$rmap[$y-1][$x]);
		}
		else
		{
		    $rmap[$y][$x] = $dmap[$y][$x] + $rmap[$y-1][$x];
		}
		
	    }
	    else
	    {
		if($x>0)
		{
		    $rmap[$y][$x] = $dmap[$y][$x] + $rmap[$y][$x-1];
		}
	    }
	}
    }
}

for my $y (0..$line)
{
    for my $x (0..$w)
    {
       print "$rmap[$y][$x]-";
    
    }
    print "\n";
}
