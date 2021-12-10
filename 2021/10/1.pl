#!/usr/bin/perl

while(<>)
{
    chomp;
    print "ytre, linja: -$_-\n";
    parse($_);    
}

my %pm = ( "(" => ")",
	   ")" => "(",
	   "\<" => "\>",
	   "\[" => "\]",
	   "\{" => "\}");

sub parse
#parse the line..: 
{
    my $str=$_[0];
#    while (true) #streng igjen
    {
#	my $first = substr $str, 0, 1;
	if ($str =~ /(^[\<\[\(\{])/)
	{
	    print "treff, -$1-\n";
	    my $l=$1;

	    my $r=parse(substr($str,1));
	    if ($pm{$l} == $r)
	    {
		print "rmatch, -$l- -".$pm{$l}."- -$r-\n";

	    }
	    else
	    {
		print "nomatch -$l- -$pm{$l}- -$r-\n";
	    }
	    #hvis venstre, husk og gå dypere uten denne.
	    # hvis retur er "samme", så er det bra, hvis ikke, skriv ut, regn.
	}
	else
	{
	    $ret=substr($str,0,1);
	    print "høyre $ret\n";
	    return $ret;
	}
    #hvis høyre: returner den.

    }
}

