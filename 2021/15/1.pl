#!/usr/bin/perl

use List::Util qw(min max);


my @dmap; # risk at point.
my @rmap; # risk from 0,0

my $w;
my $line=1;
while(<>)
{
    chomp;
    $w=length;
    my @lc=split//;
    for my $c (0..$#lc)
    {
	$dmap[$line][$0]=1000000000;
	$rmap[$line][$0]=1000000000;
	$dmap[$line][$c+1]=$lc[$c];
	$rmap[$line][$c+1]=1000000000;
    }
    $dmap[$line][$w+1]=100000000;
    $rmap[$line][$w+1]=100000000;
    
    $line++;
}
for my $x (0..$w+1)
{
    $dmap[0][$x]=100000000;
    $dmap[$line][$x]=100000000;
    $rmap[0][$x]=100000000;
    $rmap[$line][$x]=100000000;
}
$line--;




#$w--;
#$w--;

#for my $y (0..$line+1)
#{
#    for my $x (0..$w+1)
#    {
#       print "$dmap[$y][$x]-";
#    
#    }
#    print "\n";
#}

#for my $y (1..$line)
#{
#    for my $x (1..$w)
#    {
#       print "$dmap[$y][$x]";
#    
#    }
#    print "\n";
#}


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
#rr(0,0,0,200);

#iterer, se rundt. 
sub naive
{
    my $sum=0;
    for my $y (1..$line)
    {
	for my $x (1..$w)
	{
	    $rmap[$y][$x] = min($rmap[$y][$x],
				$dmap[$y][$x]+$rmap[$y][$x-1],
				$dmap[$y][$x]+$rmap[$y][$x+1],
				$dmap[$y][$x]+$rmap[$y-1][$x],
				$dmap[$y][$x]+$rmap[$y+1][$x]);
	    $sum+=$rmap[$y][$x];
	}
    }

    return $sum;
}

$rmap[1][1]=0;

my $osum=10000000000000;
my $sum=0;
while($osum!=$sum)
{
    $osum=$sum;
    $sum=naive;
#    print "o: $osum s: $sum $rmap[$line][$w]\n";
}

print "part1: $rmap[$line][$w]\n";
