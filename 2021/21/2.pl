#!/usr/bin/perl

#my @pos=(4,8);
my @pos=(1,2);
my @score;
my $die=1;
my $nrolls=0;
my $p=0;

while(($score[0] < 1000) && ($score[1] < 1000))
{
	$nrolls+=3;
	$pos[$p] = ((($pos[$p] + (($die*3)+3) % 10)-1) % 10) + 1;
	$score[$p] += $pos[$p];
	print "p $p $pos[$p] $score[$p] $die $nrolls\n";
	$die+=3;
	if ($p)
	{
	    $p=0;
	}
	else
	{
	    $p=1;
	}

}

      
