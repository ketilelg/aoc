#!/usr/bin/perl

my $line= <>;

my @draw = split(/,/,$line);


my $boardno=0;
my $lineno=-1;
my @boards;

while(<>)
{
    if($lineno >= 0)
    {
	my @tt=split(" ",$_);
	my $p=0;
	for my $x (@tt)
	{
	    $boards[$boardno][$lineno][$p] = $x;
	    $p++;
	}
	print "linje: $boardno, $lineno, $boards[$boardno][$lineno][1] -@tt-\n";
	
    }
    $lineno++;
    if($lineno > 4) { $lineno=-1; $boardno++; }


}

$boardno--;

print "draw: @draw \n";

# iterer over draw:

my @bingos; #marker hvilke brett som har bingoet.. 

my $bingo=0; #brukes for å si at ALLE har bingoet.. 

my $bb;
my $wd;

for $dr (@draw)
{
    print "dr: $dr\n";
    # iterer over alle brett, null ut alle som har verdi dr..
    for $bi (0..$boardno)
    {
	for $li (0..4)
	{
	    for $pi (0..4)
	    {
		if ($boards[$bi][$li][$pi] == $dr)
		{
		    $boards[$bi][$li][$pi] = "m";
		    
		}
	    }
	}
    }
    # sjekk om vi har en hel linje med 0, vert eller hor:
    
    for $bi (0..$boardno)
    {
	#først nedover:

	for $li (0..4)
	{
	    my $lsum=0;
	    for $pi (0..4)
	    {
		$lsum += $boards[$bi][$li][$pi];
	    }

	    if ($lsum==0)
	    {
		print "lsum0 $bi $dr!\n";
		$bb = $bi;
		$wd = $dr;
		$mybingo=1;
		last;
	    }
	}
	if ($bingo) { last; }
	# så kolonner:
	for $pi (0..4)
	{
	    my $psum=0;
	    for $li (0..4)
	    {
		$psum += $boards[$bi][$li][$pi];
	    }

	    if ($psum==0)
	    {
		print "psum0!\n";
		$bb = $bi;
		$wd = $dr;
		$mybingo=1;
		last;
	    }
	}
	if ($mybingo)
	{
	    print "bingo for brett $bi\n";
	    $bingos[$bi]=1;
	    $bingo=1;
	    for $bbi (0..$boardno)
	    {
		$bingo=$bingo && $bingos[$bbi];
				print "bingotest, $bbi -$bingos[$bbi]- -$bingo-\n";

	    }
	}
	$mybingo=0;
	if ($bingo) { last; }
    }
    if ($bingo) { last; }
}

print "bingo! $bb $wd\n";

my $bsum=0;
for $pi (0..4)
{
    for $li (0..4)
    {

	$bsum += $boards[$bb][$li][$pi];

    }
}

$m=$bsum * $wd;
print "$bsum $dr $m\n"; 
