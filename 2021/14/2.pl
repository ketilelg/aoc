#!/usr/bin/perl

use List::Util qw(min max);

my $pt = <>;
chomp $pt;

my %pir;
my %pirc; 

my %count;

while (<>)
{
    if (/(\w\w) -> (\w)/ )
    {
	$pir{$1} = $2;
    }
}

my $sc="!";
#seed pirc:
for my $c (split //, $pt)
{
    if ($pir{$sc.$c})
    {
	$pirc{$sc.$c}++;
    }
    $sc=$c;
}

for my $c (split //, $pt)
{
    $count{$c}++;
}


for my $i (1..40)
{
    my $c;
    my %npirc;
    for my $p (keys (%pirc))
    {
	$a = substr $p,0,1;
	$b = substr $p,1,1;
	$c=$pir{$p};
	$count{$c}+=$pirc{$p};
	$npirc{$a.$c}+=$pirc{$p};
	$npirc{$c.$b}+=$pirc{$p};
    }
    %pirc=%npirc;
}

my $diff=max (values %count) - min (values %count);

print "part2: $diff\n";
