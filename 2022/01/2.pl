#!/usr/bin/perl

my $max=0;
my $sum=0;


while(<>)
{
    if($_=~/(\d+)/)
    {
	$sum+=$1;
    }
    else
    {
	print "$sum\n";
	if ($sum > $max) { $max=$sum;}
	$sum=0;
    }

    
}

# print ut, sorter og summer. 
