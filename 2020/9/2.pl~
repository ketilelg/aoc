#!/opt/local/bin/perl
use Switch;
@lines = <>;

#print @lines;

my $modulus=25;
my $numlines=$.;

my $pc=0;
my $noloop=1;
my $acc=0;

my $testnum=$modulus;
while(($testnum < $numlines))
{
    my $ok=0;
    for my $i  (1..$modulus-1) {
	for my $j (2..$modulus) {
	    if (($lines[$testnum-$i] + $lines[$testnum-$j] == $lines[$testnum]) && ($i != $j)) {
		print "ok: $i $j $testnum\n";
		$ok = 1;
	    }
	}
    }
    print "ok: $ok tn: $testnum, verdi: $lines[$testnum], \n";
    $testnum++;
}
