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

	for my $mx (0..4)
	{
	    $dmap[$line][($mx*$w)+$c+1]=(($lc[$c] + $mx)-1) % 9 +1;
	    $rmap[$line][($mx*$w)+$c+1]=1000000000;
	}


    }
    $dmap[$line][$w*5+1]=100000000;
    $rmap[$line][$w*5+1]=100000000;
    
    $line++;
}

$w=$w*5;
$line--;

for my $ml (1..$line)
{
    for my $my (1..4)
    {
	for my $mx (1..$w)
	{
	    $dmap[$ml+($my*$line)][$mx] = (($dmap[$ml][$mx] + $my) -1) %9 +1;
	    $rmap[$ml+($my*$line)][$mx] = 1000000000;
	}
	$dmap[$ml+($my*$line)][0]=100000000;
	$rmap[$ml+($my*$line)][0]=100000000;
	$dmap[$ml+($my*$line)][$w+1]=100000000;
	$rmap[$ml+($my*$line)][$w+1]=100000000;
    }
}
for my $x (0..$w+1)
{
    $dmap[0][$x]=100000000;
    $dmap[$line*5+1][$x]=100000000;
    $rmap[0][$x]=100000000;
    $rmap[$line*5+1][$x]=100000000;
}

$line=$line*5;


#$w--;
#$w--;



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
    print "o: $osum s: $sum $rmap[$line][$w]\n";
}

    print "part2: $rmap[$line][$w]\n";

