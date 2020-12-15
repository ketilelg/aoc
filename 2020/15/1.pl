#!/usr/bin/perl

@lines = <>;

my $nrounds=30000000;
my @last = $nrounds;
my @prev = $nrounds;
my $numin=1;
my $ls;

chomp $lines[0];
for my $num (split /,/,@lines[0])
{
    $last{$num}=$numin;
    $prev{$num}=0;
    $ls=$num;
    $numin++;
}

for my $round ($numin..$nrounds)
{
    print "$round $ls\n";
    if ( $prev{$ls} > 0)
    {
	$ls=$last{$ls}-$prev{$ls};
    }
    else
    {
	print "\n";
	$ls=0;
    }
    $prev{$ls}=$last{$ls};
    $last{$ls}=$round;
}

print "slutt: $ls\n";
