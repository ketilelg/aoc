#!/opt/local/bin/perl
use Switch;
@lines = <>;

#print @lines;

my $pc=0;
my $noloop=1;
my $acc=0;

while($noloop) {
$lines[$pc] =~ /(\w+)\s\+?(\-?\d+)/;
if ($hasbeen[$pc]) {exit;}
print "$pc: $1 $2\n";
$hasbeen[$pc]=1;
switch($1) {
	case "acc" { $acc += $2; }
	case "jmp" { $pc += ($2-1); }
	case "nop" {}
}
print "$pc: $1 $2 acc: $acc\n";
$pc++;
}
