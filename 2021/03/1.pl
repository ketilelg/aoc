#!/usr/bin/perl

my @sum;
my @numlines;

while(<>)
{
    my @line = split (undef,$_);
    for my $i (0 .. $#line-1)
    {
	$sum[$i]+=$line[$i];
    }
	$numlines++;
}

my $gamma = 0;
my $epsilon = 0;

for my $i (0 .. $#sum)
{
    my $bitc=$sum[$i];
    print "$i $sum[$i] $bitc\n";
    if($bitc > ($numlines / 2))
    {
	$epsilon*=2;
	$gamma*=2;
	print "1";
	$epsilon++;
    }
    else
    {
	$epsilon*=2;
	$gamma*=2;
	print "0";
	$gamma++;
    }
    print "\n gamma $gamma epsilon $epsilon\n";
}

my $power=$gamma*$epsilon;
print "\n gamma $gamma epsilon $epsilon power $power\n";

