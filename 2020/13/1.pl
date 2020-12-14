#!/opt/local/bin/perl
use Switch;
@lines = <>;


my $mytime=$lines[0];
chomp $mytime;
chomp $lines[1];
for my $bus (split /,/,@lines[1]) {
    print "bus: $mytime $bus ";
    if ($bus ne "x") {
	print $bus - ($mytime % $bus);
    }
    print "\n";
}

