#!/usr/bin/perl

my $ns=0;
while (<>)
{
    @input=split /\|/;

    @res=split(" ",@input[1]);

    print "i1: @input[1] res: @res\n";

    
    foreach my $out (@res)
    {
	my $len=length($out);
	
	if ($len == 2) 
	{
	    $ns++;
	} 
	if ($len == 4)
	{
	    $ns++;
	}
	if ($len == 3)
	{
	    $ns++;
	}
	if ($len == 7)
	{
	    $ns++;
	}
	print "l: $out $len $ns\n";
    }

}
