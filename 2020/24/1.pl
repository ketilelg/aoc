#!/opt/local/bin/perl
use Switch;
my %stopped; # array av n-e, med antall stopp..
my @grid;
my $minn=200;
my $maxn=200;
my $mine=200;
my $maxe=200;

while(<>)
{
    chomp;
    #parse linja:
    my $n=200;
    my $e=200;
    my $moves=$_;

    while($moves ne "")
    {
#	print "wl: $moves $n $e\n";
	my $c=substr $moves,0,1;
	switch($c) {
	    case "n"
	    {
		if (substr($moves,1,1) eq "e")
		{ #nordøst
		    $n++;
		}
		else
		{ #nordvest
		    $e--;
		}
 		my $x=substr($moves,2);
		$moves=$x;
	    }
	    
	    case "s"
	    { #sør
		if (substr($moves,1,1) eq "e")
		{ #sørøst
		    $e++;
		}
		else
		{ #sørvest
		    $n--;
		}
 		my $x=substr($moves,2);
		$moves=$x;
	    }

	    case "e"
	    { #sørvest
		$e++;
		$n++;
		my $x=substr($moves,1);
		$moves=$x;
	    }

	    case "w"
	    {
		$e--;
		$n--;
		my $x=substr($moves,1);
		$moves=$x;
	    }
	}
#	print "we: $moves $n $e\n";


    }
    print "$_: $n $e\n";
    my $pos="$n.$e";
    $stopped{$pos}++;
    if($grid[$n][$e])
    {
	$grid[$n][$e]=0;
    }
    else
    {
	$grid[$n][$e]=1;
    }
    if($n>$maxn){$maxn=$n;}
    if($n<$minn){$minn=$n;}
    if($e>$maxe){$maxe=$e;}
    if($e<$mine){$mine=$e;}
}

my $count=0;
foreach my $stop(keys %stopped)
{
#    print "nr: $stopped{$stop} posisjon $stop: \n";
    if($stopped{$stop}==1){$count++;}
}
print "part1: $count\n";
print "$minn $maxn $mine $maxe\n";

#del2:

for my $i (1..100)
{
    my @newgrid;
    my $blacks=0;
#    print "   $minn $maxn $mine $maxe\n";
    for my $nc (($minn-1)..($maxn+1))
    {
	for my $ec (($mine-1)..($maxe+1))
	{
#	    	    print "ilo: $nc $ec \n";
	    
	    my $bb=($grid[$nc-1][$ec-1]+$grid[$nc][$ec-1]+$grid[$nc+1][$ec]+$grid[$nc+1][$ec+1]+$grid[$nc][$ec+1]+$grid[$nc-1][$ec]);
	    #	    print "ilo: $nc $ec $bb\n";
	    $newgrid[$nc][$ec]=$grid[$nc][$ec];
	    if($grid[$nc][$ec]&&($bb==0 || $bb>2))
	    {
		$newgrid[$nc][$ec]=0;
	    }
	    elsif(!$grid[$nc][$ec]&&$bb==2)
	    {
		$newgrid[$nc][$ec]=1;
	    }
	    
	}
    }
    $minn--;
    $maxn++;
    $mine--;
    $maxe++;
    for my $nc ($minn-1..$maxn+1)
    {
	for my $ec ($mine-1..$maxe+1)
	{
	    $grid[$nc][$ec]=$newgrid[$nc][$ec];
	    if($grid[$nc][$ec]) {$blacks++;}
	}
    }
    print "$i: blacks: $blacks $minn $maxn $mine $maxe\n";
}
