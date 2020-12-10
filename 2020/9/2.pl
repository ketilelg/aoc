#!/opt/local/bin/perl
use Switch;
@lines = <>;

#print @lines;

# my $secret=36845998;
my $secret=127;

my $modulus=25;
my $numlines=$.;

my $pc=0;
my $noloop=1;
my $acc=0;

my$first=0;



while(($first < $numlines))
{
    my $sum=0;
    my $i=$first;
    my $low=1000000000000;
    my $high=0;
    while(($sum<$secret)&&($i<$numlines))
    {
	my $tn=$lines[$i];		   
	$sum+=$tn;
	if ($tn > $high) {$high = $tn;}
	if ($tn < $low) {$low = $tn;}
	$i++;
    }
    if($sum==$secret){
	print "fant det: $first $i $sum $secret $low $high\n";
    }
    else
    {
#	print "fant det ikke: $first $i $sum $secret\n";
    }
    $first++
}
