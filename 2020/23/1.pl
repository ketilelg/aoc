#!/opt/local/bin/perl

use strict;

$_=<>;
chomp;
my @circle = split "";

my $len=$#circle+1;

print "lengde: $len\n";

my $position=0;



my $moves=100;
do
{
    print "\n$moves c: @circle\n";
    movit();
    $moves--;
} until ($moves==0);

print "end: @circle\n";
my $endp=0;
while ($circle[$endp] !=1)
    {
	$endp++;
    }

print "the real end @circle[$endp+1..$len-1] @circle[0..$endp-1]\n";

sub movit
{
    # trinn 1
    my @pu=@circle[1..3]; 

    print "pickup: @pu\n";
    
    #trinn 2 :
    my $nl=@circle[0];
    do
    {
	print "nlloop: $nl\n";
	$nl--;
	if ($nl < 1)
	{
	    $nl=$len;
	    print "nlif: $nl\n";
	}
    }
    until ( $nl!=@pu[0] && $nl!=@pu[1] && $nl!=@pu[2] ); # not in the three pickups

    print "nl=$nl\n";
    #find position of #nl;
    my $nlp=0;
    while ($nl != $circle[$nlp])
    {
	$nlp++;
#	print "nlpl: $nlp\n";
    }

    print "newlabel: $nl, pos: $nlp\n";

    # trinn3:
    
    my @nc;

    push(@nc,@circle[4..$nlp]);
    push(@nc,@pu);
    push(@nc,@circle[$nlp+1..$len-1]);
    push(@nc,@circle[0]);

    @circle=@nc;
}
