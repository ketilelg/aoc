#!/usr/bin/perl

my $ls=<>;
my @lut=split //,$ls;
my $ls=<>;
my $line=1;
while(<>)
{
    chomp;
    $w=length;
    my @lc=split//;
    for my $c (0..$#lc)
    {
        $map[$line][$c+1]=$lc[$c];
    }

    $line++;
    
}

print "$#lut, $w, $line\n";

$x=3;
$y=3;

my $pv=0;
for my $by($y-1..$y+1)
{
    for my $bx($x-1..$x+1)
    {
	$pv*=2;
	if ($map[$by][$bx] eq "#")
	{
	    $pv++;
	    print "#";
	}
	else
	{
	    print ".";
	}
    }
    print "\n";
}

print "$pv: -$lut[$pv]-\n";
