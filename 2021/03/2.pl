#!/usr/bin/perl

@lines = <>;

my $num= $#lines;

# les inn hele greia,
#
# iterer over bitnummer (v->h), til vi har EN verdi:
#
#    tell opp antall X-bits i denne posisjonen.
# lag en ny "greie" som kun inneholder linjer med den mest (minst) populære
# biten.
# endre bitposisjon. 
#

my $pos=0;

my @org;
@org=@lines;


while ($#lines > 0)
{
    print "ytre, $#lines\n";

    my $nbits=0;
    # finn antall 1/0 i pos. 
    for $i ( 0 .. $#lines )
    { #finn antall 1/0 i $pos
	my @line = split (undef,$lines[$i]);
	$nbits+=$line[$pos];
    }

    print "nbits: $nbits\n";
    if ($nbits > $#lines/2)
    {# mest populære bit
	$popbit=1;
    }
    else
    {
	$popbit=0;
    }
    
    my @new=();
    # lag ny array
    for $i ( 0 .. $#lines )
    { #finn antall 1/0 i $pos
	my @line = split (undef,$lines[$i]);
	if($line[$pos] == $popbit)
	{
	    push @new, $lines[$i];
	    print "pusher $lines[$i]\n";
	}
    }

    @lines=@new;
    $pos++;

}
$oxy=$lines[0];

print "orglen: $#org\n";

@lines=@org;
$pos=0;
while ($#lines > 0)
{
    print "cytre, $#lines\n";

    my $nbits=0;
    # finn antall 1/0 i pos. 
    for $i ( 0 .. $#lines )
    { #finn antall 1/0 i $pos
	my @line = split (undef,$lines[$i]);
	$nbits+=$line[$pos];
    }


    
    if ($nbits > $#lines/2)
    {# minst populære bit
	$popbit=0;
    }
    else
    {
	$popbit=1;
    }
    
    print "n1bits: $nbits $popbit\n";
    my @new=();
    # lag ny array
    for $i ( 0 .. $#lines )
    { #finn antall 1/0 i $pos
	my @line = split (undef,$lines[$i]);
	if($line[$pos] == $popbit)
	{
	    push @new, $lines[$i];
	    print "pusher $lines[$i]\n";
	}
    }

    @lines=@new;
    $pos++;
}


$co=$lines[0];

print "\nox: $oxy co2: $co\n";

$oxd= oct ("0b" . $oxy);
$cod= oct ("0b" . $co);

$res=$oxd*$cod;
print "ox: $oxd, co: $cod res=$res\n";
