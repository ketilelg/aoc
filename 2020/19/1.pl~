#!/usr/bin/perl

my @allowed; #alle tillatte tall
my %saw; #tillatte tall, indeksert pr. felt
# les regler:
my $done=0;
while(!$done)
{
    $_=<>;
    chomp;
#    print $_;

    if (/(\w+\s?\w*): (\d+)-(\d+) or (\d+)-(\d+)/)
    {
#	print " 1: $1: 2:$2 3:$3 4:$4 5:$5\n";
	for my $i ($2..$3)
	{
	    $allowed[$i]=1;
	    $saw{$1}[$i]=1;
	}
	for my $i ($4..$5)
	{
	    $allowed[$i]=1;
	    $saw{$1}[$i]=1;
	}
    }
    else
    {
	$done=1; #blank linje
    }
}
$_=<>; # skip blank
$_=<>; # skip "my ticket"
my @myticket=split ",";
print "step 2, mytick: $myticket[0]\n";

$_=<>; # skip blank
$_=<>; # skip nearby tickets
my $sum=0;
my $numticks=0;
my $numrej=0;
my @tickets;
while(<>)
{
    chomp;
    
    my @v= split ",";

    my $ok=0;
    foreach my $t (@v)
    {
#	print "fe: $t\n";
	if (!$allowed[$t])
	{
	    $sum+=$t;
#	    print "not: $t\n";
	    $ok=0;
	    last;
	}
	else
	{
	    $ok=1;
	}

    }
    if ($ok)
    {
	$tickets[$numticks] = [ @v ];
#	print "nbt: @{$tickets[$numticks]}\n";
	$numticks++
    }
    else
    {
#	print "nnot\n";
	$numrej++;
    }
}

$numticks--;

print "part1: $sum $numticks $numrej\n\n";
my @rfound;
my $w = $tickets[0];
my $n = @$w - 1;
my $ans=1;

for my $z (0..$n)
{

foreach my $k (keys %saw)
{
#    print "\nffe: $k\n";

    my $ok=1;
    my $nok=0;
    my $lastfound;
	

    for my $i (0 .. $n)
    {
	if (!$rfound[$i])
	{
#	    print "pos: $i\n";
	    my $ok=1;
	    for my $j (0..$numticks)
	    {
		my $v=$tickets[$j][$i];
#		print "il $j $i $v ";
		$ok=$ok&$saw{$k}[$v];
#		print " ok: $ok\n";
	    }
	    if ($ok)
	    {
#		print "loop $k $i\n";
		$nok++;
		if ($nok == 1) {$firstfound=$i;}

#	    $saw{$k}=[];
#	    last;
	    }

	}
    }


    if ($nok == 1)
    {
	$rfound[$firstfound]=1;
	
#        print "el: $nok $k $firstfound\n";
	if ($k=~/departure/)
	{
	    $ans*=$myticket[$firstfound];
	    print "dep: $k $myticket[$firstfound] $ans\n";
	}

    }
}
}
