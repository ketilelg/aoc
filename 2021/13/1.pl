#!/usr/bin/perl

my @map;
my @fid;
my @fiv;
my $fs=0;
my $maxx,$maxy;

while(<>)
{
    if (/(\d+),(\d+)/)
    {
	$map[$1][$2]=1;
	if ($1 > $maxx) { $maxx = $1; }
	if ($2 > $maxy) { $maxy = $2; }
    }
    if (/^fold along (\w)=(\d+)/)
    {
	$fid[$fs]=$1;
	$fiv[$fs]=$2;
	$fs++;
    }
}


sub printmap
{
    for my $y (0..$maxy)
    {
	for my $x (0..$maxx)
	{
	    if ($map[$x][$y])
	    {
		print "#";
	    }
	    else
	    {
		print ".";
	    }
	}
	print "\n";
    }
    
}

sub countmap
{
    my $r=0;
    for my $y (0..$maxy)
    {
	for my $x (0..$maxx)
	{
	    if ($map[$x][$y])
	    {
		$r++;
	    }
	}
    }
    return $r;
}

sub foldy
{
    my $fy=$_[0];
    for my $y (0..$fy-1)
    {
	for my $x (0..$maxx)
	{
	    if ($map[$x][$maxy-$y])
	    {
		$map[$x][$y] = 1;
	    }
	}
    }
    $maxy=($maxy/2) - 1;
}

sub foldx
{
    my $fx=$_[0];
    for my $x (0..$fx-1)
    {
	for my $y (0..$maxy)
	{
	    if ($map[$maxx-$x][$y])
	    {
		$map[$x][$y] = 1;
	    }
	}
    }
    $maxx=($maxx/2)-1;
}


for my $i (0..$fs-1)
{
    if ($fid[$i] eq "y")
    {
	foldy($fiv[$i]);
    }
    else
    {
	foldx($fiv[$i]);
    }

}

my $r=countmap;
print "part1: $r\n";
printmap;
