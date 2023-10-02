#!/usr/bin/perl

use strict;

my %edges; #indeksert pr tile. hver inneholder liste over kanttall..

my %it; #inner tiles, brukes i del2..


#les inn tiles: de er 10x10:
while (<>)
{
    chomp;
    if(/Tile\s(\d+):/)
    {
	my @tile;
	my $lstr;
	my $rstr;
	my $tileno=$1;
#	print "tile: $tileno\n";
	for my $i (0..9)
	{
	    $_ = <>;
	    chomp;
	    s/\#/1/g;
	    s/\./0/g;
	    $tile[$i]=$_;
	    $lstr.=substr $_,0,1;
	    $rstr.=substr $_,9,1;
	    if(($i>0)&&($i<9))
	    {
		$it{$tileno}[$i] = substr $_,1,8;
	    }
#	    print; print "\n";
	}
	# top bottom left right. norm reverse.
	
	my $tn= oct("0b$tile[0]");
	my $x=reverse $tile[0];
#	print "rev- .$tile[0]. .$x\n.";
	my $tr= oct("0b$x");

	my $rn= oct("0b$rstr");
	my $x=reverse $rstr;
	my $rr= oct("0b$x");

 	my $br= oct("0b$tile[9]");
	my $x=scalar reverse $tile[9];
	my $bn= oct("0b$x");
	
	my $lr= oct("0b$lstr");
	my $x=reverse $lstr;
	my $ln= oct("0b$x");
	
	$edges{$tileno}=" $tn $rn $bn $ln R $tr $rr $br $lr ";


	print "tileno $tileno:\n $tn\n $rn\n $bn\n $ln\nR\n $tr\n $rr\n $br\n $lr\n";
    }
}

my $r1=1;
my $corner;
my $numtiles;
my %hits; #husker hvilke sider som er truffet, indexert på tile. treff uten speil
my %rhits; #husker speilede treff.
my %thits; #husker alle treff..

foreach my $t (keys %edges)
{
    # har denne tilen naboer?
    my $hit=0;
    my $hn=0;
    # vi sjekker pr. kant:
    for my $e (split " ",$edges{$t})
    {
	if(($hn < 4))
	{ #men bare ikke-reversert. vi treffer jo reverserte i de andre:
#		print "for $e\n";
	for my $s (keys %edges)
	{
	    if (($t ne $s) && ($edges{$s}=~/.*\s$e\s.*R.*/))
	    { #funnet en nabo.. men er den snudd eller ikke? 
		$hit++;
#		print "s hit: $hn\n";
		$hits{$t}.=" $hn $s ";
		$thits{$t}.=" $hn $s ";
	    }
	    if (($t ne $s) && ($edges{$s}=~/.*R.*\s$e\s.*/))
	    { #funnet en nabo.. men er den snudd eller ikke? 
		$hit++;
#		print "r hit: $hn\n";
		$rhits{$t}.=" $hn $s ";
		my $tttt=$hn+4;
		$thits{$t}.=" $tttt $s ";
	    }
	}
	}
	$hn++;
    }
    if($hit == 2)
    {
	$r1*=$t;
	$corner=$t;
    }

    print "$hit $t: $edges{$t} ";
    print "fe $t - S:$hits{$t} R:$rhits{$t} T: $thits{$t}\n";

    $numtiles++
}

print "part1: $r1\n";

# vi vet at $corner er et hjørne. vi erklærer det ul. så går vi ut fra at hele greia
# er roten av numtiles stor.

my @map; # hele kartet. er nxnx8 strenger a 8 tegne

print "nt: $numtiles\n";
my $size=sqrt($numtiles);
print "size: $size\n";

my @tnmap; # x*y tabell over tiles.
my %rfmap; # tile- tabell over rotasjon og flip: 0,1,2,3: roter 0,90,180,270. +4: flip opp/ned
my %taken; # tabell over teatte ting. satt om tatt. trenger vi?

copytile(0,0,$corner);

$tnmap[1][1]=$corner; # ok, passert. men hva med rotasjon?
# vi finner ut hvilke retninger vi er truffet:

my $rh= () = ($rhits{$corner}=~/(\d\s+\d+)/g); #hvor mange hits i reverse?
my $h1; #første treff 0=t, etc..
my $h2; #2.treff.
$rfmap{$corner}=0;
if($rh==0)
{
    $hits{$corner}=~/(\d)\s(\d+)\s+(\d)\s(\d+)/g;
    print "$1 $2 -1 $3 $4\n";
    $h1=$1;
    $h2=$3;
}
elsif ($rh==1)
{
    $hits{$corner}=~/(\d)\s(\d+)/g;
    print "$1 $2";
    $h1=$1;
    $rhits{$corner}=~/(\d)\s(\d+)/g;
    print " -2 $1 $2\n";
    $h2=$1;
}
else #$rh=2
{
    $rhits{$corner}=~/(\d)\s(\d+)\s+(\d)\s(\d+)/g;
    print "$1 $2 -3 $3 $4\n";
    $h1=$1;
    $h2=$3;
#    $rfmap{$corner}=4;
}

    $thits{$corner}=~/(\d)\s(\d+)\s+(\d)\s(\d+)/g;
    print "$1 $2 sdf $3 $4\n";

print "corner: $corner : .$hits{$corner}. R .$rhits{$corner}.  r: $rh h1: $h1 h2: $h2 $1 $3\n";

if($h1==0 && $h2==1) {$rfmap{$corner}+=1;} 
if($h1==2 && $h2==3) {$rfmap{$corner}+=2;} 


#vi jobber i en grid som er 2 større i begge retninger. Så $count posisjoneres slik:
# (count har origin i 0. men vi juksar lite, og spsifikt plasserer første hjørne. (linjene over)
# x=($count % size) +1
# y =(int($count/$size) +1

my $count=1;
do
{
    my $x=($count % $size)+1;
    my $y=(int($count / $size) + 1);

    #skal vi se venstre eller opp?
    if($x==1)
    { #vi skal se opp
	#vi må finne kanten som peker mot oss. altså nr 2 i x,y-1:

	my $neig = $tnmap[$x][$y-1]; #naboen vi skal titte på..:

	
	
    }
    else
    {#vi ser til venstre, altså x-1, y
	my $neig = $tnmap[$x-1][$y]; #naboen vi skal titte på..:

#	my @ee = $edges{$neig} =~ /
    }
    
#    print "$x $y\n";

    $count++;
} while ($count<$numtiles);



sub copytile
{
    my $x=$_[0];
    my $y=$_[1];
    my $tileno=$_[2];
#    #tar x, y, tileno som input. kopierer tileno til gitt pos. i map rotasjon??
#    for my $i (1..8)
#    {
#	$map[$x][$y][$i] = $it{$tileno}[$i];
#    }
#    
}
