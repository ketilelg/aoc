#!/opt/local/bin/perl
use Switch;
@lines = <>;

@sorted = sort {$a <=> $b} @lines;

for $j  (0..@sorted) { print "$j: $sorted[$j]\n"; }

my $numlines=$.;

my $pc=0;

my $i=1;
my @diffs;

while(($i < $numlines))
{
    $diffs[($sorted[$i]-$sorted[$i-1])]++;
    $i++;
}

for $j  (0..@diffs) { print "$j: $diffs[$j]\n"; }
