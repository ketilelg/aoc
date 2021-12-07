#!/usr/bin/perl

@crabs=split(",", <>);


my $sum;
my $min=1000000;
my $max=0;
my $shortest=100000000;
foreach my $c (@crabs)
{
    $sum+=$c;
    if ($min > $c) {$min=$c;}
    if ($max < $c) {$max=$c;}
}

for my $c ($min..$max)
{
    my $sd=0;
    foreach my $cc (@crabs)
    {
	#finn sumavstand
	$dist=abs($cc-$c);
	    $cost=($dist*($dist+1))/2;
	    $sd+=$cost;
#	    print "dist $dist $cost\n";
    }
#    print "c: $c sd: $sd\n";
    if ($shortest>$sd) {$shortest=$sd;}
}

$avg= $sum/($#crabs+1);
print "sum: $sum, avg: $avg $min $max shortest: $shortest\n";
