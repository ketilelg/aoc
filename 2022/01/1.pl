#!/usr/bin/perl

my $max=0;
my $sum=0;


while(<>)
{
    if($_=~/(\d+)/)
    {
	print "linje: $1\n";
	$sum+=$1;
    }
    else
    {
	print "tom linje, $sum\n";
	if ($sum > $max) { $max=$sum;}
	$sum=0;
    }

    
}

print "max: $max\n";
