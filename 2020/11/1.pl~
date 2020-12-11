#!/usr/bin/perl
#
# forutsetter at input inneholder start og slutt (0, og siste+3)

@lines = <>;

@sorted = sort {$a <=> $b} @lines;


my @diffs;
my $diffstr;

for my $i (1..$#sorted)
{
    my $diff=($sorted[$i]-$sorted[$i-1]);

    $diffs[$diff]++;
    $diffstr.=$diff;
}

for $j  (0..@diffs) { print "$j: $diffs[$j]\n"; }

my $p1=$diffs[1]*$diffs[3];
print "part1: $p1\n";

print "\ndiffstr: $diffstr\n";
my $m = ($diffstr =~ s/1111//g);
my $perm=7**$m;
my $m = ($diffstr =~ s/111//g);
$perm*=4**$m;
my $m = ($diffstr =~ s/11//g); 
$perm*=2**$m;
print "perm: $perm\n";

