#!/usr/bin/perl

@lines = <>;

my %last;
my %prev;
my $numin=1;
my $ls;

chomp $lines[0];
for my $num (split /,/,@lines[0])
{
    print "num: $num\n";
    $last{$num}=$numin;
    $prev{$num}=0;
    $ls=$num;
    $numin++;

}
print "lest: $numin\n";
for my $round ($numin..30000000)
{
#    print "$round $ls";
    if ( $prev{$ls} > 0)
    {
#	print " ja: $ls $prev{$ls} $last{$ls} ";
	$ls=$last{$ls}-$prev{$ls};
	$prev{$ls}=$last{$ls};
	$last{$ls}=$round;
	#	print " --- $ls $prev{$ls} $last{$ls}\n";
#	print "$round: $ls\n";
    }
    else
    {
#	print " nei 0 $prev{$ls} $last{$ls} \n";
	$ls=0;
	$prev{$ls}=$last{$ls};
	$last{$ls}=$round;
    }
}

print "slutt: $ls\n";
