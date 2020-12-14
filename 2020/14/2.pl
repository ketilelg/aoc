#!/usr/bin/perl
use Switch;

my %memory;

my $andb;
my $orb;
my $mask;
my $numx;
while(<>)
{
#    print $_;
    chomp;


    /(\w+)/;

    switch($1) {
	case "mask" {
	    /\w+\s=\s(\w+)/;
	    $mask=$andm=$orm=$1;
	    #	    $mask=reverse("$1");
	    
	    $andm=~s/0/1/g;
	    $numx=($andm=~s/X/0/g);
	    $orm=~s/X/0/g;
	    
	    $andb = oct( "0b$andm" );
	    $orb = oct( "0b$orm" );
#	    print " cmask $numx $andb $orb $mask\n";
	}
	case "mem" {

	    /mem\[(\d+)\]\s=\s(\d+)/;
	    assignto($numx + 1,$mask,($1&$andb),$2);
#	    $memory[$1] = ($2 & $andb) | $orb;
#	    print " cmem  $1 $2 $memory[$1]\n";

	}
	
    }

}
my $sum;
foreach my $key (keys %memory )
{
#    print "fe: $memory{$key}\n";
    $sum+=$memory{$key};
}
print "sum: $sum\n";


sub assignto
{
    #tar nbits, maske som streng, memadr, value  som input
    #går rekrusivt til det ikke er bits igjen å flippe. setter så
    #mem til verdien. 
    my $ns=$_[0];
    $ns--;
#    print "a: $ns,$_[1],$_[2],$_[3]\n";
    if ($ns == 0) {
	my $nm=$_[1];
	my $orm=oct("0b$nm");
	my $addr=$_[2]|$orm;
	$memory{$addr} = $_[3];
#	print "am: $orm $nm $addr = $_[3] \n";
    }
    else
    { # > 0, altså
#	my $exp= 2**(35-index($_[1],'X'));
	#	print "at: $exp\n";
	my $nmask=$_[1];
	my $npos=index($nmask,'X');
	substr($nmask,$npos,1)='1';
#	print "at: $ns $nmask $npos\n";
	assignto($ns,$nmask,$_[2],$_[3]);
	substr($nmask,$npos,1)='0';
	assignto($ns,$nmask,$_[2],$_[3]);
    }
}
