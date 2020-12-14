#!/opt/local/bin/perl
use Switch;

my @memory;

my $andb;
my $orb;
while(<>)
{
    chomp;
    print $_;

    /(\w+)/;

    switch($1) {
	case "mask" {
	    /\w+\s=\s(\w+)/;
	    $andm=$orm=$1;
	    $andm=~s/X/1/g;
	    $orm=~s/X/0/g;
	    $andb = oct( "0b$andm" );
	    $orb = oct( "0b$orm" );
	    print " cmask $andb $orb \n";
	}
	case "mem" {
	    /mem\[(\d+)\]\s=\s(\d+)/;
	    $memory[$1] = ($2 & $andb) | $orb;
	    print " cmem  $1 $2 $memory[$1]\n";

	}
	
    }

}
my $sum;
foreach ( @memory )
{
    $sum+=$_;
}
print "sum: $sum\n";
